
import torch
import time

def test_binary_classification(dataloader, model, loss_fn, device="cpu") -> tuple:
    """
    Binary classification validation/evaluation function
    
    [parameter]
        dataloader: DataLoader - The dataloader for validation dataset
        model: The model to be evaluated
        loss_fn: The loss function to compute the difference between model predictions and true labels
        device: str - The device to run computations on
    [return]
        tuple: (loss, accuracy)
    """
    model = model.to(device)
    model.eval() # Set model to evaluation mode
    size = len(dataloader.dataset)
    num_steps = len(dataloader)
    
    test_loss, test_accuracy = 0., 0.
    
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            y = torch.tensor(y).unsqueeze(dim=-1).type(torch.float32) # Increase dimension [64,]
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            ## Calculate accuracy
            pred_label = (pred >= 0.5).type(torch.int32)
            test_accuracy += (pred_label == y).sum().item() 
            
        test_loss /= num_steps
        test_accuracy /= size   # Divide by total number of samples
    return test_loss, test_accuracy
    
def train(dataloader, model, loss_fn, optimizer, device="cpu", mode:"binary or multi"='binary'):
    """
    Train the model for one epoch

    [parameter]
        dataloader: DataLoader - Dataloader providing training dataset
        model - The model to be trained
        loss_fn: The loss function to compute the difference between model predictions and true labels
        optimizer - The optimization function
        device: str - The device to run computations on. default-"cpu", gpu-"cuda"
        mode: str - Classification type. binary or multi
    [return]
        tuple: Train loss and accuracy after training the model
    """
    model = model.to(device)
    model.train()
    size = len(dataloader.dataset) 

    for X, y in dataloader:
        X, y = X.to(device), y.to(device)
        y = torch.tensor(y).unsqueeze(dim=-1).type(torch.float32) # Increase dimension [64,]
        pred = model(X)

        loss = loss_fn(pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if mode == 'binary':
        train_loss, train_accuracy = test_binary_classification(dataloader, model, loss_fn, device)
    else:
        train_loss, train_accuracy = test_multi_classification(dataloader, model, loss_fn, device)
    return train_loss, train_accuracy
    
def fit(train_loader, val_loader, model, loss_fn, optimizer, epochs, save_best_model=True, 
        save_model_path=None, early_stopping=True, patience=10, device="cpu",  
        mode:"binary or multi"='binary',
        lr_scheduler=None):
    """
    Train the model

    [parameter]
        train_loader (Dataloader): Train dataloader
        test_loader (Dataloader): validation dataloader
        model (Module): The model to be trained
        loss_fn (Loss): Loss function
        optimizer (Optimizer): Optimizer
        epochs (int): Number of epochs
        save_best_model (bool, optional): Whether to save the model if performance improves during training. Defaults to True.
        save_model_path (str, optional): Path to save the model when save_best_model=True. Defaults to None.
        early_stopping (bool, optional): Whether to use early stopping. Defaults to True.
        patience (int, optional): Number of epochs to wait before stopping if no performance improvement. Defaults to 10.
        device (str, optional): The device to run computations on.
        mode(str, optinal): Classification type. "binary(default) or multi
         lr_scheduler: Learning Scheduler object default=None      ====> Adjust the learning rate at the end of each epoch
    [return]
        tuple: Lists of performance for each epoch. (train_loss_list, train_accuracy_list, validation_loss_list, validataion_accuracy_list)
    """

    train_loss_list = []
    train_accuracy_list = []
    val_loss_list = []
    val_accuracy_list = []
    
        
    if save_best_model:
        best_score_save = torch.inf

    ############################
    # early stopping
    #############################
    if early_stopping:
        trigger_count = 0
        best_score_es = torch.inf
    
    # Move model to the device
    model = model.to(device)
    s = time.time()
    for epoch in range(epochs):
        train_loss, train_accuracy = train(train_loader, model, loss_fn, optimizer, device=device, mode=mode)
       
        # Adjust the learning rate using the scheduler after each epoch
        if lr_scheduler is not None:
            c_lr = lr_scheduler.get_last_lr()[0]  # The current learning rate before adjustment
            lr_scheduler.step()  # learning rate update
            n_lr = lr_scheduler.get_last_lr()[0]  # The new learning rate after adjustment
            if c_lr != n_lr:
                print(f"####### Learning rate changed from {c_lr} to {n_lr}.")

        
        if mode == "binary":
            val_loss, val_accuracy = test_binary_classification(val_loader, model, loss_fn, device=device)
        else:
            val_loss, val_accuracy = test_multi_classification(val_loader, model, loss_fn, device=device)

        train_loss_list.append(train_loss)
        train_accuracy_list.append(train_accuracy)
        val_loss_list.append(val_loss)
        val_accuracy_list.append(val_accuracy)
        
        print(f"Epoch[{epoch+1}/{epochs}] - Train loss: {train_loss:.5f} Train Accucracy: {train_accuracy:.5f} || Validation Loss: {val_loss:.5f} Validation Accuracy: {val_accuracy:.5f}")
        print('='*100)
        
        # Save the model if performance improves
        if save_best_model:
            if val_loss < best_score_save:
                torch.save(model, save_model_path)
                print(f"<<<<<<<Saved: {epoch+1} - Previous : {best_score_save}, Current: {val_loss}")
                best_score_save = val_loss
        
         # Early stopping handling           
        if early_stopping:
            if val_loss < best_score_es:  # Performance improvement (Yes)
                best_score_es = val_loss  
                trigger_count = 0
                                
            else: # No performance improvement (No)
                trigger_count += 1                
                if patience == trigger_count:
                    print(f">>>>>>Early stopping: Epoch - {epoch}")
                    break
            
    e = time.time()
    print(e-s, "seconds")
    return train_loss_list, train_accuracy_list, val_loss_list, val_accuracy_list
