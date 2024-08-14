import sys
from transformers import pipeline

def main():
    # 如果传递了命令行参数，使用它们作为输入
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        # 如果没有传递命令行参数，使用默认的输入
        text = "The Transformers library provides thousands of pretrained models."

    # 使用Hugging Face的pipeline进行文本分类
    classifier = pipeline("sentiment-analysis")

    # 对文本进行分类
    result = classifier(text)

    # 输出结果
    print(f"Input: {text}")
    print(f"Sentiment: {result[0]['label']}, Confidence: {result[0]['score']:.4f}")

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       