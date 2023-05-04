import argparse
import json
import datetime
import os

'''
orig_data: {"instruction": "题目：小明买了一支钢笔，花费了5元，又买了一本书，花费8元，现在他手里还有10元钱，他手上原来有多少钱？", "input": "", "output": "\n令小明手上原来有的钱为X元。根据题目描述，得出以下方程式：\nX - 5 - 8 = 10\n化简可得：\nX = 23\n因此，小明手上原来有23元钱。"}
convert: {
    "id": xxx,
    "conversations":[
        {"from": "human", "value": "题目：小明买了一支钢笔，花费了5元，又买了一本书，花费8元，现在他手里还有10元钱，他手上原来有多少钱？"},
        {"from": "assistant", "value": "\n令小明手上原来有的钱为X元。根据题目描述，得出以下方程式：\nX - 5 - 8 = 10\n化简可得：\nX = 23\n因此，小明手上原来有23元钱。"},
    ]
}
'''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--orig_data",
    )
    parser.add_argument(
        "--write_data",
    )
    parser.add_argument(
        "--dataset_name",
    )
    args = parser.parse_args()
    with open(args.write_data,"w") as f_write:
        with open(args.orig_data) as f:
            lines = f.readlines()
            for num_id, line in enumerate(lines, start=1):
                data = json.loads(line)
                conversations = [{"from": "human", "value": data['instruction']+data['input']},{"from": "assistant", "value": data['output']}]
                            # conversations = [{"from": "human", "value": data['input']},{"from": "assistant", "value": data['target']}]
                uniq_id = data['id'] if "id" in data else f"{args.dataset_name}-{str(num_id)}"
                item = {"id":uniq_id, "conversations": conversations}
                f_write.write(json.dumps(item, ensure_ascii=False)+"\n")


if __name__ == "__main__":
    main()