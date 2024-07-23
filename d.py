def classify_flammability(material):
    # 물질별 인화점 정보
    flash_points = {
        "휘발유": -43,
        "아세톤": -20,
        "이황화탄소": -30,
        "등유": 38,
        "니트로벤젠": 88
    }

    # 인화점에 따른 점수 분류 기준
    if material in flash_points:
        flash_point = flash_points[material]
        if flash_point >= 60:
            return 1
        elif 30 <= flash_point < 60:
            return 2
        elif 0 <= flash_point < 30:
            return 3
        elif -20 <= flash_point < 0:
            return 4
        elif flash_point < -20:
            return 5
    else:
        return "알 수 없는 물질입니다."


# 사용자 입력 받기
material_name = input("물질 이름을 입력하세요: ")
score = classify_flammability(material_name)
print(f"{material_name}의 인화점 분류 점수는: {score}점입니다.")
