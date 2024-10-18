def get_face_keypoints(img_dir): 
    """
    Parameter
        img_dir : 한 시나리오 폴더의 img_dir
    Return 
        img_xy_list : 한 시나리오(25장)에 대해 얼굴 68개 keypoints에 대한 xy좌표 중첩 리스트로 반환
    """
    import glob
    import PIL
    from PIL import Image
    import cv2
    import mediapipe as mp
    import os
    import numpy as np

    # keypoints index 
    landmark_points_68 = [162,234,93,58,172,136,149,148,152,377,378,365,397,288,323,454,389,71,63,105,66,107,336,
                  296,334,293,301,168,197,5,4,75,97,2,326,305,33,160,158,133,153,144,362,385,387,263,373,
                  380,61,39,37,0,267,269,291,405,314,17,84,181,78,82,13,312,308,317,14,87]

    # mp_face_mesh 객체 생성
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(
        static_image_mode=False, # 정적 이미지 
        max_num_faces=1,    
    )

    # 한 시나리오의 좌표 리스트 누적
    img_xy_list= []

    # 이미지 디렉토리 경로에서 하위 경로 리스트 생성
    img_path_list = glob.glob(os.path.join(img_dir,"**/*.jpg"), recursive=True)

    # 이미지 읽기  
    for img_path in img_path_list:
        frame = Image.open(img_path)
        frame = cv2.resize(np.array(frame), (400, 600))

        # 얼굴 검출
        results = face_mesh.process(frame)
        
        # 한 이미지의 눈 좌표 리스트 ; 한 이미지 끝나고 돌 때 초기화
        img_kp_list=[]

        if results.multi_face_landmarks: # 얼굴 감지됐는지 확인 #
            for idx, landmark in enumerate(results.multi_face_landmarks[0].landmark): # 운전자 1명, 리스트에서 빼기
                if idx in landmark_points_68:
                    x = landmark.x 
                    y = landmark.y 
                    img_kp_list.append((x,y))
               
            img_xy_list.append(img_kp_list)
        else:
            break              

    return img_xy_list
