# 테스트 설계 보고서

## 1. 모델 평가 기준
  - 정량 평가 : 정확도, Loss(Binary CrossEntropy Loss)      
  - 정성 평가 : 실시간 영상을 입력 받아 운전자의 졸음 판별 테스트
        
## 2. 테스트 환경
  - 하드웨어(GPU- GEForce rtx 2080super, 메모리 - 16GB)
  -  소프트웨어: PyTorch, OpenCV, YOLO

      
## 3. 테스트 결과

![학습결과그래프](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/assets/156928146/20bd0017-ef6c-421b-80a4-8346d75bc65d)
![학습결과](https://github.com/Playdata-G-DA35/DA35-4th---DriverDrowsinessDetection/assets/156928146/f830faa2-4d26-4cc1-a426-8a97ce633216)

- Valid Accuracy : 99%
- Valid Loss : 0.02%
