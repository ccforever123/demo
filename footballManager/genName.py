import random

def randomName():
    nameCount = random.randint(2, 3)
    firstNameList = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '姚', '邵', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴',  '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '诸葛', '司马']
    # firstNameList = ['陈']
    name = random.sample(firstNameList, 1)[0]
    for i in range(nameCount-1):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)
        val = f'{head:x}{body:x}'
        selectChs = bytes.fromhex(val).decode('gb2312')
        # selectChs = chr(random.randint(0x4e00, 0x9fbf))
        name = name + selectChs
    return name

if __name__ == '__main__':
    for i in range(30):
        name = randomName()
        print(name)