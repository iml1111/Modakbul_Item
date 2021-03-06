# Modakbul_Item
세종대학교 SW융합대학 홈페이지 "모닥불"

## INTRO
![img](https://gblobscdn.gitbook.com/assets%2F-Lk4yfhdwc6qCX9Adhlj%2F-LlJIOasCvZpom6IZv8i%2F-LlJJh6Vdg-5IQw8zz2l%2Fimage.png?alt=media&token=bcacc680-dbd3-4408-a389-1c5176913694)
본 프로젝트는 소프트웨어융합대학 제 3대 학생회 "번영"에서 주최하는 공모전 "웹으로 소융대를 설명하라"를 위해 수행된다. 
공모전의 주제로 기존의 소프트웨어 융합 대학 웹 페이지를 분석하고 개선점을 도출한 후,  
해당 솔루션을 바탕으로 새로운 웹 서비스를 개발한다.  

본 프로젝트를 수행함으로써, 보다 선진적인 디자인 및 구조를 통해 세종대학교 소융대의 위상을 높이고, 
향후 소융대 재학생 및 구성원들 간의  정보 공유가 증진될 것이라 기대한다.

# 프로젝트 추진 배경 및 필요성

‌

공모전의 룰에 따라 기존 "번영" 학생회가 운영하고 있는 소융대 홈페이지를 분석하였고 몇 가지 문제점을 찾을 수 있었다. 대표적인 문제점은 다음과 같다.

# 시스템 구조

![img](https://gblobscdn.gitbook.com/assets%2F-Lk4yfhdwc6qCX9Adhlj%2F-LlHTRkkpElHP9rwNGOo%2F-LlHsY1TwD809BqhXhjX%2Fimage.png?alt=media&token=0f00c3ca-2e50-42c1-b7ae-edfc2dbe2a07)



# **기존의 문제점**

‌

## 메인 페이지 포스트

![img](https://gblobscdn.gitbook.com/assets%2F-Lk4yfhdwc6qCX9Adhlj%2F-LkAHtZY3SefqGQtBKpb%2F-LkAKCaadtPQFRDmlgg6%2Fimage.png?alt=media&token=1cb2efc9-f87d-49df-9db8-e699f59b5d73)

‌

메인 페이지는 “번영” 학생회를 명시하는 로고 이미지로 인한 공간 낭비가 존재한다.  이미지 슬라이드 기능이 존재하지만, 본질적으로 전혀 사용되지 않고 있으며, 학생회를 나타내는 비슷한 이미지를 열거하고 있을 뿐이다. 해당 로고를 효과적으로 명시하면서 남은 공간을 다른 기능에 활용할 여지가 존재한다.

‌

## 메인 페이지 최근 글

![img](https://gblobscdn.gitbook.com/assets%2F-Lk4yfhdwc6qCX9Adhlj%2F-LkAHtZY3SefqGQtBKpb%2F-LkAKQ0pkq_Z2i8hHiyt%2Fimage.png?alt=media&token=c46dbfa1-39c5-413c-be13-99e2d3bb17b6)

‌

위 사진은 “번영” 학생회 홈페이지의 메인 화면이다. 메인 페이지에 가장 최근에 게시된 글을 보여주는 것은 매우 자연스러운 인터페이스이지만 그저 제목을 row 기반의 테이블 형식으로 나열하는 것은 가독성 측면에서 좋은 선택이 아니다.  해당 게시물과 관련된 이미지 및 글의 분류를 통해 고유의 태그(개인이 정의하는 해쉬태그 X) 등을 정의하는 등으로 각 게시판의 가독성을 높일 필요가 있다.  또한, 해당 글은 최근 글이라는 명칭을 하고 있지만 모든 글이 아닌, 최근에 작성된 공지사항을 표시하고 있다. 해당 페이지에는 공지사항 외에도, 각 학과별 회비 사용내역, 민원게시판, 갤러리, 공모전 홍보 등의 다양한 정보를 메인 페이지에서 간결하게 확인할 수 있도록 최근 글 기능을 개선해야 한다.

‌

## 불필요하게 작은 검색 화면

![img](https://gblobscdn.gitbook.com/assets%2F-Lk4yfhdwc6qCX9Adhlj%2F-LkAKia8Hkh3_CR9zQGa%2F-LkAKrb8_jhLc8bZ8lyL%2Fimage.png?alt=media&token=1a66f20a-268c-4e56-92f6-0370ceec6636)

‌

상대적으로 사용 빈도가 높은 검색 기능에 대한 인터페이스 크기가 너무 작다. 한 번에 검색 텍스트를 작성할 수 있도록 하거나, 별도의 모달을 통해 검색 인터페이스를 크게 명시할 필요가 있다. 또한 익스플로러에서 툴팁과 같은 몇몇 기능이 지원되지 않았다.

‌

## 게시물 접근 통제 기능 부재

![img](https://gblobscdn.gitbook.com/assets%2F-Lk4yfhdwc6qCX9Adhlj%2F-LkAKia8Hkh3_CR9zQGa%2F-LkAL7KKAoIKBm9Fiwm9%2Fimage.png?alt=media&token=d1aff912-cc06-4d60-b326-5c36fdeb7e1f)

‌

누구나 모든 게시물에 대한 자유로운 접근이 가능하며, 따로 읽기 권한을 제한할 수 있는 기능이 제공되지 않는다. 이를 통한 각 활동에 대하여 불필요한 개인 정보의 유출이 일어날 수 있다.

‌

## 불편한 모바일 인터페이스

![img](https://gblobscdn.gitbook.com/assets%2F-Lk4yfhdwc6qCX9Adhlj%2F-LkAKia8Hkh3_CR9zQGa%2F-LkALMfnAYWxMF7t0GF0%2Fimage.png?alt=media&token=9b211834-271e-4a92-8bf0-6008f3afc37a)

‌

모바일 기기를 통한 기능에서 사용이 불가능하거나 사용하는 데에 불편한 점이 몇몇 존재한다. 대표적으로 모바일 환경에서 몇몇 기기에서 내용 작성 폼이 뜨지 않아 글 작성이 불가능했으며, 게시글 하나의 영역이 충분히 넓음에도 제목 부분을 클릭해야하만 게시 글을 확인할 수 있는 점이 존재한다.

‌

## 게시되는 정보량 부족 및 커뮤니티 공간 부재

‌

해당 홈페이지는 현재 소융대 전체를 대상으로 하는 공지사항 및 소융대 자체 주최의 공모전 등의 한정된 정보 밖에 게시되지 않기 때문에 상대적으로 타 사이트에 비해 적은 방문자수를 보여준다.  소융대 재학생들은 기본적으로 소프트웨어라는 공통의 주제가 존재하기 때문에 이것을 토대로 사용자들을 끌어들일 만한 유용한 정보(대외활동, 공모전, 전공 지식, 기타 정보 공유)를 게시하는 공간을 마련할 수 있을 것이다.

‌

## **익명 게시 기능 부재**

‌

해당 게시물의 작성자에 대한 익명 게시 기능이 존재하지 않는다.


본 프로젝트에서는 위의 문제 사항을 개선하고, 소융대 재학생들 간의 정보 공유가 더 효율적으로 수행될 수 있도록 소프트웨어 융합 대학 커뮤니티 “모닥불”을 개발한다.

# 모닥불의 스키마

![img](https://gblobscdn.gitbook.com/assets%2F-Lk4yfhdwc6qCX9Adhlj%2F-LkANS9fbeZHAAav-nZT%2F-LkAMubL-o66QF-kv6Al%2Fimage.png?alt=media&token=290e0064-57d6-45d8-8f8a-619a120f54f2)

‌

# 모닥불의 특징

‌

모닥불은 세종대학교 소융대를 위한 웹 서비스로,  기존의 문제점을 개선하기 위한 프로젝트이다. 모닥불은 대표적으로 다음과 같은 특징을 가진다.

‌

- 학교 포탈 시스템을 통한 구성원 인증
- 학교 이벤트 및 관심사에 대한 투표 및 설문조사 기능
- 소융대 구성원 커뮤니티
- 학과 관련 대외활동을 비롯한 각종 정보 크롤링 및 게시
- 보다 편리한 관리자 인터페이스
- 사용자 통계 기능을 통한 빅데이터 수집 및 시각화





**포탈 시스템을 통한 간편한 로그인!**

‌

- **학교 포탈 시스템을 통한 구성원 인증** 대부분의 교내 커뮤니티 사이트는 개별적으로 회원가입을 하거나 타 SNS와의 Oauth 통신을 통해서 개별적인 인증 체계를 갖추게 된다. 모닥불은 실제 학교 포탈 시스템과 연동하여 직접 인증 절차를 거침으로써 사용자는 포탈 계정으로 보다 쉽게 접근할 수 있으며, 신속하게 인증 과정을 진행할 수 있다.



**직관적이고 거슬리지 않는 설문조사!**

‌

- **학교 이벤트 및 관심사에 대한 투표 및 설문조사  기능** 소융대 구성원을 대상으로 관심사에 대한 투표 및 설문 기능을 제공한다. 기존의 이러한 직관적인 설문 기능을 제공하는 서비스가 존재하지 않았기 때문에 대부분 구글 폼 등의 외부 서비스를 사용할 수 밖에 없었던 점을 극복하기 위함이다. 



**소융대 구성원에 알맞는 게시판!**

‌

- **소융대 구성원 커뮤니티** 소융대 구성원들이 사용할 수 있는 커뮤니티 공간을 제작한다. 여기에는 기본적인 자유 게시판, 민원 게시판을 포함하여, 단대 특성상 소프트웨어에 관심있는 사용자들을 고려하여 코드 블럭을 지원하는 지식인 게시판을 포함할 계획이다.



 **외부 대외활동 정보를 한눈에!**

‌

- **학과 관련 대외활동을 비롯한 각종 정보 크롤링 및 게시** 마찬가지로 단대의 특성상, 공모전 및 취업 관련 정보에서 어느정도 일관된 관심사를 띄게 된다. 그를 통해 외부 웹사이트에서 관련 정보를 수집하여 모닥불에서 게시함으로 보다 접근성을 강화한다.



**모닥불 서비스는 개발자가 죽어도 지속되어야 한다**!

‌

- **보다 편리한 관리자 인터페이스** 해당 서비스는 학교 내부 웹 사이트로써 지속적으로 유지되어야 하는 특성상, 해당 관리자가 시스템의 구조를 모르더라도 대부분의 기능을 통제할 수 있도록 매우 직관적인 인터페이스를 제공해야 한다. 



**사용자의 액션과 흐름을 한눈에 담자!**

‌

- **사용자 통계 기능을 통한 빅데이터 수집 및 시각화** 모닥불에서 수행된 사용자의 모든 액션을 수집화하고 해당 데이터를 시각화한다. 이를 통해 소융대 구성원이 무엇에 관심을 가지고 있는지 등의 유의미한 정보를 도출하고 활용함으로 단대의 발전에 기여할 수 있을 것이다.
