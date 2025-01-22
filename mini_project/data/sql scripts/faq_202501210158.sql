/* Create the FAQ table */
CREATE TABLE faq (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-increment primary key
    question TEXT NOT NULL,             -- Question column
    answer TEXT NOT NULL                -- Answer column
);

INSERT INTO faq (question,answer) VALUES
	 ('Kia Digital Key(NFC)란 무엇인가요?','Kia Digital Key는 NFC 안테나가 장착된 스마트폰 또는 카드 키로 차량의 도어를 열고 시동을 걸 수 있는 새로운 서비스입니다.Kia Digital Key NFC 카드 키Kia Digital Key NFC 카드 키는 최초 1회 차량 등록 후 사용 가능하며, 도어 핸들에 카드를 태그 하여 차량에 출입하실 수 있습니다.출입 후, 무선 충전 패드에 카드를 거치한 뒤 차량의 시동을 걸 수 있습니다.NFC 카드 키 등록 방법'),
	 ('직영 서비스센터 운영 시간은 어떻게 됩니까?','직영 서비스센터의 업무시간은 평일(월~금) 08:30~17:30까지 이며, 중식시간은 12:30~13:30 입니다.직영서비스센터는 예약제로 운영되므로 방문 전 사전 예약 바랍니다.토탈 예약 센터 안내 (1899-0200)전화 한통으로 고객님과 가장 가까운 서비스 네트워크에서 정비서비스를 받을 수 있도록 사전 예약을 접수하고 있습니다.AUTO Q 검색/예약'),
	 ('사용설명 분실했는데 어떻게 재발급 받을 수 있나요?','사용설명서 분실 및 중고차 구입을 하신 경우에는 기아멤버스 홈페이지를 통해 보실 수 있습니다.사용 설명서'),
	 ('내 차 관리를 위한 필수 앱, MyKia는 어떤 서비스 인가요?','나만의 꼼꼼한 개인비서, 더욱 강화된 개인화 서비스· 날씨, 차량 상태를 포함 사용자 데이터 기반 개인 맞춤형 화면과 콘텐츠를 제공합니다.· 차량 운행 후 안전운전 점수 및 운전 습관 데이터를 MyKia를 통해 확인해 보세요.· 정기 점검, 보증 및 리콜 정보까지 꼼꼼하게 챙겨주고, 가까운 정비소 검색과 손쉬운 예약을 도와줍니다.* 서비스 이용은 차종 및 사양에 따라 상이할 수 있으며, 일부 서비스는 datahub 서비스 가입 및 이용 동의 필요더욱 똑똑해진 차계부로, 스마트하고 편리한 ''차량관리''· 정비 이력 확인, 소모품 관리, 주유/EV  충전 내역, 자동차 할부 정보 등 내 차와 관련된 모든 비용을 한눈에 관리할 수 있습니다.· 항목별, 월별 리포트를 통해 지출 내역을 점검하고 전월과 비교하여 소비습관을 확인해 보세요.EVerything for EV, EV 고객을 위한 특화 서비스· 기아 EV 멤버스 가입 하나로, 충전 걱정 끝!  충전 로밍 서비스와 구독형 충전 요금제, 이 모든 것을 기아멤버스 포인트로 결제할 수 있는 EV멤버스 혜택까지 EV고객만을 위한 다양한 특화 프로그램과 차별화된 혜택을 제공합니다.기아 온라인 통합 회원을 위한 다양한 혜택과 이벤트· MyKia에 가입한 하나의 ID로 기아에서 제공하는 다양한 서비스를 이용하실 수 있습니다.(기아닷컴, 기아멤버스 홈페이지, 기아 디지털 키, Kia Connect 등)* 기아 디지털 키, Kia Connect 등 일부 서비스는 별도 서비스 가입 및 이용 동의 필요'),
	 ('기아 통합 계정이 무엇인가요?','기아 통합 계정은, 기아닷컴 / 기아멤버스 홈페이지 / MyKia 모바일 앱 / 기아 디지털키 / Kia Connect 등 기아에서 제공하는 서비스를 사용하기 위한 계정으로, 하나의 ID로 모든 서비스를 이용할 수 있습니다.* 단, 로그인 후 각 서비스 별로 추가적인 서비스 가입이 필요합니다.* 기아닷컴 / 기아멤버스 홈페이지 / MyKia에 가입 시도 시, 정상적으로 가입이 이루어지지 않은 경우에는 기타 서비스(Kia Connect 등)의 가입 여부를 먼저 점검해 보시기 바랍니다. 타 서비스 가입 이력이 있다면 별도 가입 절차 없이 해당 ID로 로그인 및 서비스 이용 가능합니다.'),
	 ('일반 리모컨 또는 스마트 키 차량의 핸들 락(잠김) 해제 방법을 알려주세요','일반 리모컨 적용 차량 또는 이모빌라이져 적용 차량의 핸들락(잠김) 해제방법① 왼손으로 핸들을 잡고 오른손으로 키셋트에 키를 꽂는다② 핸들을 좌우로 힘껏 움직이면서 동시에 ACC 방향으로 키를 돌린다.스마트키 차량의 경우 시동과 동시에 핸들락(잠김)이 해제됩니다.'),
	 ('전자식 파킹 브레이크(EPB) 기능이 무엇인가요?','전자 파킹 브레이크(EPB : Electronic Parking Brake)는페달 또는 레버로 케이블을 당겨 파킹 브레이크를 작동시키는 대신 스위치 조작으로 모터 구동을 통해 파킹 브레이크를 작동함으로써 운전자 편의성 향상을 도모하는 시스템입니다.전자식 파킹 브레이크 작동 방법· 차량 정지 상태에서 전자식 파킹 브레이크 스위치를 당기면 전자 파킹 브레이크가 체결· 전자식 파킹 브레이크가 정상적으로 체결되면 계기판에 브레이크 경고등 점등전자식 파킹 브레이크 해제 방법① 수동해제· 전자 파킹 브레이크(EPB)가 체결된 상태에서, 스위치를 당겨 해제할 수 있습니다.· 단, 아래의 모든 조건이 만족되는 경우에 해제가 가능합니다.(시동 버튼 「ON」 위치일 때, 브레이크 페달을 밟은 상태)② 자동해제· 변속기가 「P」(주차)단에 위치하고 주차 브레이크가 체결되어 있는 경우,엔진이 켜진 상태에서 브레이크 페달을 밟고 자동변속기 레버를 「P」(주차)단에서  「R」/「N」/「D」단으로 변속하면 전자 파킹 브레이크(EPB)가 자동으로 해제됩니다.· 또한, 아래의 모든 조건을 만족된 경우 가속 페달을 천천히 밟아 해제할 수 있습니다.(엔진이 켜져 있고 운전자 안전벨트를 착용한 상태, 운전석 도어/엔진 후드 및 트렁크가 닫힌 상태, 자동변속기 레버가 「R」/「D」 또는 수동모드에 있는 경우)'),
	 ('버튼시동 스마트 키 차량의 경우 중립 주차는 어떻게 합니까?','버튼시동 스마트 키 차량의 경우 D/R/N 단 위치에서 시동을 끌 경우 ACC 상태가 되어  전원이 꺼지지 않고 스마트키로 도어를 잠글 수 없습니다. 다른 사람이 차량을 움직일 수 있도록 주차시켜 놓을 때는(중립 주차) 차량 사양에 따라 다음과 같이 사용해주시기 바랍니다.변속레버 앞쪽에 「SHIFT LOCK RELEASE」버튼이 있는 차종① 주차 브레이크를 걸고, 브레이크 페달을 밟은 상태에서 「P」(주차) 위치에 두고 엔진을 끄십시오.스마트키 장착 차량은 「P」(주차) 위치에서만 시동버튼을 「OFF」상태로 전환할 수 있습니다.② 주차 브레이크를 푸십시오.③ 브레이크 페달을 밟고 변속레버 앞쪽에 위치한 「SHIFT LOCK RELEASE」버튼을 누른 상태에서 변속 레버를 「N」(중립) 위치로 이동하십시오. 차량을 밀어서 움질일 수 있는 상태가 됩니다.변속레버 앞쪽에 「SHIFT LOCK RELEASE」버튼이 없는 차종(일부 차량의 경우 쉬프트락 해제 버튼 없음)① 주차 브레이크를 걸고, 브레이크 페달을 밟은 상태에서 「P」(주차) 위치에 두고 엔진을 끄십시오.스마트키 장착 차량은 「P」(주차) 위치에서만 시동버튼을 「OFF」상태로 전환할 수 있습니다.② 주차 브레이크를 푸십시오.③ 브레이크를 밟고 자동변속기를 「N」(중립)위치로 두십시오.「P」(주차)는 변속기가 잠기는 위치로, 차를 쉽게 움직일 수 없는 위치입니다.* 자세한 내용은 취급설명서를 참조하시기 바랍니다.'),
	 ('스마트 키 배터리 교환방법에 대해 알려주세요','스마트 키의 사용횟수와 기간에 따라 배터리 성능이 저하되었을 경우 배터리 교환이 필요합니다.배터리 교환 시 차종별 스마트 키 배터리 용량을 확인 후 배터리를 구입하여 교환하시면 됩니다.① 리모컨 키(스마트 키)의 옆면 또는 아랫면에 일자 모양의 홈이 있습니다.이 홈에 동전이나 일자 드라이버(-)와 같은 도구를 끼우신 후 살짝 비틀어 주시면 스마트키 뒷면의 건전지 커버가 분리되며, 내부에 동그란 수은 배터리가 확인 됩니다.② 스마트키 규격에 맞는 새 배터리를 구입하셔서 교환하시면 됩니다.수은 배터리는 대형 마트, 문구점에서 구입하실 수 있습니다.③ 조립은 분해의 역순으로 하시면 됩니다.배터리를 장착하신 후, 스마트키 뒷면의 건전지 커버를 장착해 주시기 바랍니다.단, 스마트 키 내부의 회로는 정전기 등에 약하며, 직접 교체가 어려운 경우 오토큐에서 점검 및 교환을 의뢰하시기 바랍니다.'),
	 ('내비게이션 업데이트는 어디서, 어떻게 하나요?','내비게이션 업데이트는 기아멤버스 홈페이지에 접속하시어 이용하실 수 있습니다.업데이트 시 유의사항① 시동 스위치 ON 하여 내비게이션이 켜진 경우에도 업데이트 가능합니다.(주의 : 차량 전원을 사용하는 경우 배터리 충전량이 충분한 상태에서 업데이트를 진행하는 것을 권장합니다.)② 업데이트 중 내비게이션 전원이 차단되거나, 미디어를 제거할 경우 정상 동작하지 않을 수 있습니다.(주의 : 시동 버튼 ON 상태에서 업데이트 중 시동을 걸 경우에도 내비게이션 전원이 차단될 수 있습니다.)* 도로/카메라/명칭/주소/전화번호 등의 신규 지도 등록 또는 오류가 있다면 아래 URL을 클릭하시어 제보해 주십시오.내비게이션/빌트인 캠 업데이트지도개선요청');
