# 딥러닝 활용 졸음운전 실시간 감지 모델 개발

## 1. 주제

딥러닝을 활용한 졸음운전 실시간 감지 

## 2. 프로젝트 목적 및 목표

- 목적 : 졸음운전 사고로 인해 인명피해와 교통 혼잡 문제를 막기 위해 운전 중 졸음 상태를 실시간으로 감지해 사고를 예방
- 목표 : 실시간 졸음 운전 감지 시스템 개발

## 3. 데이터 설명

1. 사용 데이터 
- 졸음운전 예방을 위한 운전자 상태 정보 영상   
- 출처 : [데이터 찾기 - AI 데이터찾기 - AI-Hub (aihub.or.kr)](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=173)
- 데이터 정보
    - 준통제환경 데이터 활용
         실제 승용 차량에서 일반운정 상황과 부주의 운전 상황을 시나리오에 따라 사람의 연기를 통해 연출하여 영상 데이터
        
    - 타입 : 이미지
         각 시나리오 영상(2분)에서 25프레임씩 추출 - 약 4.8초 간격
        
    - 크기 : 21750 장
        - 정상 : 7250장 ,  약간 졸음: 7250 장, 졸음 : 7250장
    - train / valid / test 비율  - 8 : 1 : 1
    
2. 데이터 전처리 과정 및 방법
    1. 라벨링을 위한 이미지 분류
        - 데이터 디렉토리명에서 ‘시나리오 번호’를 기준으로 이미지 분류
        - 운전자 상태 시나리오 5개를 `정상 / 통화 / 흡연 / 하품 / 졸음` 를 `정상 / 약간 졸음 / 졸음` 3개 클래스로 재분류
                

| 라벨  | 클래스 분류 | 시나리오 분류 |
| --- | --- | --- |
| 0 | 정상 | 정상, 통화, 흡연 |
| 1 | 조금 졸림 | 하품 |
| 2 | 졸음 | 졸음 |


- 
    2. 얼굴 Keypoints 추출  
    - Mediapipe Face Landmark 활용
        - 총 468개의 얼굴 keypoints 중 68개 선정
        - 68개 keypoints의 x,y좌표 추출
    - 시나리오 폴더 내 사진 25장 모두에서 얼굴 keypoints 가 인식된 경우만 선택
        - 한 시나리오 폴더는 2분 동안 4.8초 간격으로 캡처된 운전자의 얼굴 이미지가 25장 있음.
        - 시나리오 내에 누락된 이미지가 있을 경우, 연속적인 sequential 데이터로 생성할 수 없기 때문임.
    3. 학습 데이터 생성
    - 얼굴 keypoints 좌표값을 추출하여 클래스별 DataFrame 생성
    -  레이블 인코딩
          - 디렉토리 명의 시나리오 번호 기준
          - 0 - normal , 1- little drowsy, 2 - drowsy
    -  이미지 내 얼굴 keypoints 좌표값 누적 데이터프레임 생성
          - shape : (21750, 136)
          - 행 : 4.8초 간격으로 캡처한 Frame 이미지
          - 열 : 얼굴 keypoints 136개 좌표(X) + 라벨(y)
    - 같은 시나리오 내에서 sliding window 방식
        - sequential length  = 5
        - 운전자 졸음 상태 판정 최소 단위 : 4.8초 * 5 = 24초   
        - X  : 얼굴 keypoints 136개 (x좌표 68개, y좌표 68개)
        - y :  라벨 (0 - 정상, 1 - 약간 졸음,  2- 졸음)


## 4.  모델링 기법
### 4-1. 모델링 기법 후보 
- 고려한 모델링 기법
    1. Keypoint Detection → LSTM → FCL   **사용**
    2. CNN → LSTM → FCL 
    
- Keypoint Detection 을 통한 특징 추출 선택 이유
    
     1. 눈, 입외에도 졸음으로 얼굴 주요 부위의 크기 및 위치가 변화하기 때문
     2. 연산이 가벼워 실시간 영상 처리 적용에 적합
    
- 고려한 Keypoint Detection Framework
    - Mediapipe, openpose, dlib, yolo
    - 패키지 설치 용이, fine tuning 없이 사용할 수 있는 Mediapipe face landmark 사용

### 4-2. 모델 구조
- Pre-trained 모델 사용하지 않고 직접 설계
- 구조
    - LSTM : sequential data의 특징 추출
    - Dropout layer :  과적합 방지
    - Sequential block : `Linear`, `Batch Norm1`, `ReLU`로 구성
    - 최종 출력 : 다중분류 (3개 노드)로 구성
    - 총 파라미터 수 : 27,971
  ![image](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/assets/156928146/2f8d2707-b62f-4a8c-a31f-89c8912c0760)

