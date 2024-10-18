import os
import pandas as pd
import numpy as np
import random
import warnings
from get_face_keypoints_fn import get_face_keypoints

warnings.filterwarnings("ignore", category=UserWarning)

# 시나리오 번호
normal = [1, 8, 15, 20, 27]
phone = [4, 5, 11, 12, 18, 19, 23, 24, 30, 31]
smoke = [6, 7, 13, 14, 25, 26]
yawn = [3, 10, 17, 22, 29]
drowsy = [2, 9, 16, 21, 28]

def split_scenarios(dirname):
    """
    시나리오별 파일 리스트를 구분하여 반환

    Parameters
        dirname (str): 파일이 위치한 디렉토리 경로

    Returns
        tuple: (drowsy_scn, yawning_scn, phone_scn, smoke_scn, normal_scn)
    """
    path_list = os.listdir(dirname)
    drowsy_scn = []
    yawning_scn = []
    phone_scn = []
    smoke_scn = []
    normal_scn = []

    for path in path_list:
        scn = int(path.split("_")[4])  # 시나리오 번호 추출

        if scn in drowsy:
            drowsy_scn.append(os.path.join(dirname, path))
        elif scn in yawn:
            yawning_scn.append(os.path.join(dirname, path))
        elif scn in phone:
            phone_scn.append(os.path.join(dirname, path))
        elif scn in smoke:
            smoke_scn.append(os.path.join(dirname, path))
        else:
            normal_scn.append(os.path.join(dirname, path))

    return drowsy_scn, yawning_scn, phone_scn, smoke_scn, normal_scn

def generate_csv(dirname, num_sample =290):
    """
    시나리오별로 데이터를 분할하고 CSV 파일 생성

    Parameters
        dirname (str): 파일이 위치한 디렉토리 경로
        num_sample (int) : 샘플 폴더 개수
    """
    # 시나리오별 파일 리스트 가져오기
    drowsy_scn, yawning_scn, phone_scn, smoke_scn, normal_scn = split_scenarios(dirname)

    # 시나리오별 파일 리스트에서 랜덤으로 섞기
    random.seed(42)
    random.shuffle(drowsy_scn)
    random.shuffle(yawning_scn)
    normal_all_scn = random.sample(smoke_scn, 150) + random.sample(phone_scn, 150) + random.sample(normal_scn, 150)
    random.shuffle(normal_all_scn)

    # 데이터 프레임 생성
    normal_0_df = create_df_fn(normal_all_scn, 0, num_sample)  # 총 450개
    yawning_1_df = create_df_fn(yawning_scn, 1, num_sample)    # 총 375개
    drowsy_2_df = create_df_fn(drowsy_scn, 2, num_sample)      # 총 376개


    print("CSV 파일 생성 완료.")

def create_df_fn(scn_path, scn, num_sample=290):
    """
    Parameter
        scn_path : random shuffle한 디렉토리 경로 (drowsy_scn, yawning_scn, normal_all_scn 중에 받음)
        scn : 0 - 정상, 1 - 하품, 2 - 졸음 
        num_sample : 시나리오  폴더 개수 

    Return 
        scenario_df 
            행 : scenario내 모든 이미지
            열 : 얼굴 68개 keypoints xy 좌표 
    """
    import numpy as np
    
    cnt = 0  # 25장 모두 인식한 디렉토리 수  
    scenario_df = pd.DataFrame()  # 이전 DataFrame을 저장할 빈 데이터 프레임 생성

    # 45개 랜덤 경로의 이미지(get_face_keypoints 함수) 얼굴 좌표 리스트 받기
    for i, img_path in enumerate(scn_path): 
        if cnt <= num_sample - 1:  # 사진을 모두 인식한 시나리오가 45개인 동안 반복
            img_xy_list = get_face_keypoints(img_path)
    
            # list를 ndarray 변환
            img_xy_np = np.array(img_xy_list)
            num_img, num_keypoints, _ = img_xy_np.shape
            # print(f"Number of frames: {num_img}, Number of keypoints: {num_keypoints}")
    
            if num_img == 25:  # 25장 이하이고 cnt가 45개 이하면 사용 
                x_df = pd.DataFrame(img_xy_np[:, :, 0])  # 68개 keypoints x좌표
                y_df = pd.DataFrame(img_xy_np[:, :, 1])  # 68개 keypoints y좌표
                current_df = pd.concat([x_df, y_df], axis=1, ignore_index=True)
            
                # label값 주기  # 0 - 정상, 1- 조금 졸음, 2- 졸음
                current_df['label'] = scn
            
                # 이전 df와 현재 df concat
                scenario_df = pd.concat([scenario_df, current_df], axis=0, ignore_index=False)
                cnt += 1
            
        else:
            break
        
    # status 정의
    if scn == 0:
        status = "normal"
    elif scn == 1:
        status = "little drowsy"
    else:
        status = "drowsy"
        
    # 디렉토리 생성
    output_dir = "scenario_df"
    os.makedirs(output_dir, exist_ok= True)
    
    # 데이터 프레임 저장 
    save_path = os.path.join("scenario_df", f"scn_{scn}_{status}.csv")
    scenario_df.to_csv(save_path, index=False)
    print(f">>>>>>>>>>>>>>>>>>>>>모든 이미지 인식에 성공한 {status}[{scn}] scenario 폴더 수 : {cnt}개")
    
    return scenario_df

def load_scenario_csv(scenario_dir, scn_type, scn_label):
    """
    CSV 파일로부터 데이터 프레임을 로드하는 함수

    Parameters
        scenario_dir (str): 시나리오 CSV 파일이 저장된 디렉토리 경로
        scn_type (int): 시나리오 타입 (0, 1, 2)
        scn_label (str): 시나리오 레이블 (normal, little drowsy, drowsy)

    Returns
        pd.DataFrame: 불러온 데이터 프레임
    """
    try:
        filename = f"scn_{scn_type}_{scn_label}.csv"
        df = pd.read_csv(os.path.join(scenario_dir, filename))
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

def create_sq_data(df, time_steps=5):
    """
    Parameter
        dataframe : df_0_normal + df_1_little drowsy + df_2_drowsy 통합
        time_step : 하나의 sequence 길이

    Return 
        data_X
        data_y
    """
    X = df.drop(columns="label").values
    y = df['label'].values
    
    data_X = []  # shape : [timesteps, 136]
    data_y = []  # output data 모을 리스트 
    
    num_range = []
    # 하나의 시나리오에서 10장씩(50초) - 16개의 시퀀스가 나옴.
    for idx in range(0, y.size - time_steps + 1):  # 행이 10개 남을 때까지 반복
        for i in range(25 * (idx + 1) - time_steps, 25 * (idx + 1) + 1):  # 15부터 25까지
            num_range.append(i)
            
        if idx not in num_range:
            _X = X[idx:time_steps + idx]
            _y = y[idx]
           
            data_X.append(_X)
            data_y.append(_y)
    
    data_X = np.array(data_X)
    data_y = np.array(data_y)
    
    return data_X, data_y
