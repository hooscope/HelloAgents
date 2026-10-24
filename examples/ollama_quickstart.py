"""使用项目根目录 .env 配置的 Ollama 模型运行一次对话。"""

from dotenv import load_dotenv
from hello_agents import HelloAgentsLLM, SimpleAgent


def main() -> None:
    load_dotenv()
    llm = HelloAgentsLLM()
    agent = SimpleAgent(
        name="本地助手",
        llm=llm,
        system_prompt="你是一个简洁的中文助手，请用中文回答。",
    )
    print(agent.run("你好，请用一句话介绍你自己。"))


if __name__ == "__main__":
    main()
