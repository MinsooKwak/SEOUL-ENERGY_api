# WEB APP | SEOUL-ENERGY

한국전력거래소가 지난 12월 6일 제공한 서울시 전력 거래량 데이터를 기반으로 거래량 예측 모델을 만들었습니다.
본 데이터는 2021년 1월~ 10월까지의 5개의 원자료 (LNG, 바이오, 연료전지, 태양광, 패기물)의 약 300일간의 전력거래량을 포함합니다.

본 프로젝트는 데이터파이프라인을 전반적으로 구축하는 것에 초점이 맞춰져 있으며, 
다중선형모델을 사용합니다.
본 데이터는 300일정도의 정보를 담고 있지만, 11월 12월의 데이터를 포함한 1년단위의 데이터가 누적된다면 더 좋은 예측이 가능할 것이라 생각됩니다.

### 1. Data Pipeline
![002](https://user-images.githubusercontent.com/89770691/145943757-6206033a-e9af-46dc-87dd-c33a26bdb413.jpg)

### 2. Model
![006](https://user-images.githubusercontent.com/89770691/145943998-c5e4cbd9-b705-4277-a9a1-23aef7deff36.jpg)

### 3. SEOUL-ENERGY 서비스
![007](https://user-images.githubusercontent.com/89770691/145944191-2bececfa-7340-461f-8664-a7ae072b198e.jpg)

### 4. SEOUL-ENERGY
SEOUL-ENERGY의 배포된 web-app을 첨부합니다.
https://seoul-energy.herokuapp.com/
