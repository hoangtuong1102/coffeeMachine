MENU = {
    "den": {
        "nguyen lieu": {
            "nuoc": 50,
            "sua" : 100,
            "coffee": 18,
        },
        "gia": 100,
    },
    "den da": {
        "nguyen lieu": {
            "nuoc": 200,
            "sua": 150,
            "coffee": 24,
        },
        "gia": 130,
    },
    "nau da": {
        "nguyen lieu": {
            "nuoc": 250,
            "sua": 100,
            "coffee": 24,
        },
        "gia": 150,
    }
}
loi_nhuan = 0

resources = {
    "nuoc": 300,
    "sua": 200,
    "coffee": 100,
}

def check_tai_nguyen(do_uong):
    for ten_san_pham in do_uong:
        if do_uong[ten_san_pham] > resources[ten_san_pham]:
            print(f"{ten_san_pham} khong du")
            return False
    return True

def tien_xu():
    total = 0
    print("Nhap so tien vao day")
    total  = int(input("Nhap so dong xu 500: ")) *500
    total += int(input("Nhap so dong xu 100: "))*100
    total += int(input("Nhap so dong xu 50: "))*50
    total += int(input("Nhap so dong xu 10: "))*10
    return (total)

def da_nhan_du_tien_chua(so_tien_nhan, gia_san_pham):
    if so_tien_nhan > gia_san_pham:
        change = so_tien_nhan - gia_san_pham
        print(f"bo may tra lai may {change}")
        global loi_nhuan
        loi_nhuan += gia_san_pham
        return True
    else:
        print("Ban deo du tien")

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"day la mon {drink_name} cua may")

is_on = True
while is_on:
    choice = input("may muon uong gi? (den/den da/nau da): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"nuoc : {tai_nguyen['nuoc']} ml")
        print(f"sua : {tai_nguyen['sua']} ml")
        print(f"coffe : {tai_nguyen['coffee']} ml")
    else:
        drink = MENU[choice]
        if check_tai_nguyen(drink["nguyen lieu"]):
            so_tien_nhan = tien_xu()
            if da_nhan_du_tien_chua(so_tien_nhan, drink["gia"]):
                make_coffee(choice, drink["nguyen lieu"])




