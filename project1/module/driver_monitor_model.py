import torch
import torch.nn as nn

class DriverMonitorModel(nn.Module):
    """
        input_size: LSTM input_size, 
        hidden_size: LSTM hidden_size
        num_layers: LSTM stack layer 개수
        bidirectional: 양방향 여부
        dropout_rate: LSTM의 dropout 비율.
    """
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False, dropout_rate=0.0):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_size, 
            hidden_size=hidden_size, 
            num_layers=num_layers,
            bidirectional=bidirectional,
            dropout=dropout_rate
        )
        D = 2 if bidirectional else 1
        self.dropout = nn.Dropout(dropout_rate)
        self.l1 = nn.Sequential(nn.Linear(in_features=hidden_size * D, out_features=128), nn.BatchNorm1d(128), nn.ReLU())
        self.l2 = nn.Sequential(nn.Linear(in_features=128, out_features=64), nn.BatchNorm1d(64), nn.ReLU())
        self.l3 = nn.Sequential(nn.Linear(in_features=64, out_features=32), nn.BatchNorm1d(32), nn.ReLU())
        self.l4 = nn.Linear(in_features=32, out_features=3)
        
    def forward(self, X):
        X = X.permute(1, 0, 2)
        out, (hidden, cell) = self.lstm(X)
        last_out = out[-1, :, :]
        last_out = self.dropout(last_out)
        last_out = self.l1(last_out)
        last_out = self.l2(last_out)
        last_out = self.l3(last_out)
        last_out = self.l4(last_out)
        return last_out