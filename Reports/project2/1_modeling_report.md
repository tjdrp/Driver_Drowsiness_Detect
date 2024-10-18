## 1. 주제

딥러닝을 활용한 졸음운전 실시간 감지 

## 2. 프로젝트 목적 및 목표

- 목적 : 졸음운전 사고로 인해 인명피해와 교통 혼잡 문제를 막기 위해 운전 중 졸음 상태를 실시간으로 감지해 사고를 예방
- 목표 : 실시간 졸음 운전 감지 시스템 개발

## 3. 데이터 설명

1. 사용 데이터 
- 졸음감지를 위한 눈 사진 영상
- 출처 : https://www.kaggle.com/datasets/kutaykutlu/drowsiness-detection
- 데이터 정보        
    - 타입 : 이미지(.png)
    - 크기 : 48000장
    - train / valid / test 비율  - 8 : 1 : 1
    
3. 데이터 전처리 과정 및 방법
  1. 이미지를 150x150 크기로 resize
  2. 이미지를 grascale로 변환 (단일 채널)
  3. 이미지를 텐서로 변환
  4. 텐서 값을 평균 0.5, 표준편차 0.5로 정규화

## 4.  모델링 기법
### 4-1. 모델 구조 
- Pre-trained 모델 사용하지 않고 직접 설계
- 구조
    - 특징추출기 : Conv2d - BatchNorm2d - ReLU - Dropout - MaxPool2d 
    - 추론기 : Flatten - Linear - ReLU - Dropout - Linear
    - 레이어 수 : 25
    - 노드 수 : 64
    - 총 파라미터 수 : 830,849
      ![모델구조](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/assets/156928146/4aac58e1-4fbf-4ca5-8a4a-c210bda196f7)


### 4-2. 모델 학습 
- 하이퍼파라미터 튜닝
    - Batch_size 변경
    - Convolution layer out_feature값 변경
    - resize로 이미지 크기 변경
    - RGB → GrayScale 이미지 채널 변경
    - Epoch 수 변경
    - 위와 같은 값들을 변경하며 모델을 학습시킨 결과 가장 높은 정확도와 낮은 loss율을 비교함


