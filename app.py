import os
import ast
import operator
import streamlit as st
import wikipediaapi
from smolagents import CodeAgent, DuckDuckGoSearchTool, tool, LiteLLMModel

st.set_page_config(
    page_title="GAIA AI Agent",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
    <style>
        .main { background-color: #0e1117; }
        .stTextInput>div>div>input {
            background-color: #1e1e2e;
            color: white;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 GAIA AI Agent")
st.markdown("**Powered by Groq LLaMA 3.3 70B + smolagents**")
st.markdown("---")
st.markdown("🔍 Web Search &nbsp;&nbsp; 📖 Wikipedia &nbsp;&nbsp; 🔢 Calculator")
st.markdown("---")

with st.sidebar:
    st.header("⚙️ Settings")
   api_key = os.environ.get("GROQ_API_KEY","")
if not api_key:
    api_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_xxxxxxxxxxx"
    )
    st.markdown("Get your key at [console.groq.com](https://console.groq.com)")
    st.markdown("---")
    st.markdown("**Tools Available:**")
    st.markdown("- 🔍 DuckDuckGo Web Search")
    st.markdown("- 📖 Wikipedia")
    st.markdown("- 🔢 Safe Calculator")
    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

@tool
def wikipedia_search(query: str) -> str:
    """
    Searches Wikipedia and returns a summary of the topic.
    Use this for factual questions, history, science, people, places.
    Args:
        query: The topic to search on Wikipedia
    """
    try:
        wiki = wikipediaapi.Wikipedia(
            user_agent="GAIA-AI-Agent/1.0",
            language="en"
        )
        page = wiki.page(query)
        if page.exists():
            summary = page.summary
            return summary[:1500].rsplit('.', 1)[0] + '.'
        return "No Wikipedia page found for this topic."
    except Exception as e:
        return f"Wikipedia error: {str(e)}"

@tool
def calculate(expression: str) -> str:
    """
    Safely evaluates a mathematical expression.
    Use this for any arithmetic or math calculations.
    Args:
        expression: A math expression like '25*48' or '100/4+5'
    """
    allowed_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod
    }

    def eval_node(node):
        if isinstance(node, ast.Constant):
            return node.n
        elif isinstance(node, ast.BinOp):
            op = type(node.op)
            if op not in allowed_ops:
                raise ValueError("Operator not allowed")
            return allowed_ops[op](eval_node(node.left), eval_node(node.right))
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -eval_node(node.operand)
        raise ValueError("Unsupported expression")

    try:
        tree = ast.parse(expression, mode='eval')
        result = eval_node(tree.body)
        return f"{expression} = {result}"
    except Exception:
        return "Invalid expression. Example: '25*48' or '100/4'"

@st.cache_resource
def load_agent(key):
    model = LiteLLMModel(
        model_id="groq/llama-3.3-70b-versatile",
        api_key=key
    )
    return CodeAgent(
        tools=[DuckDuckGoSearchTool(), wikipedia_search, calculate],
        model=model,
        max_steps=6,
        verbosity_level=0
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask GAIA anything..."):
    if not api_key:
        st.error("⚠️ Please enter your Groq API Key in the sidebar!")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("🤖 GAIA is thinking..."):
                try:
                    agent = load_agent(api_key)
                    answer = agent.run(prompt)
                    st.markdown(answer)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer
                    })
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
