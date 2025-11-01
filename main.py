# main.py
from flask import Flask, render_template

# Vercel 建议所有 Flask 应用实例都命名为 'app'
# static_folder 和 template_folder 使用默认值即可
app = Flask(__name__)

# 导入配置
# from app.core._config import load_config # 示例

# 导入您的路由文件
# 注意：导入时需要使用 Python 包的绝对路径
try:
    from app.routes._dnsLookup import dns_bp  # 假设您使用了蓝图
    app.register_blueprint(dns_bp)
except ImportError:
    # 如果您没有使用蓝图，而是直接在 _dnsLookup.py 中定义路由
    # 确保 _dnsLookup.py 中的路由装饰器指向的是这里的 'app' 实例
    pass

# 定义主页路由
@app.route('/', methods=['GET', 'POST'])
def index():
    # 您的主页逻辑
    return render_template('index.html', title='DNS Lookup Tool')

# -------------------------------------------------------------
# 额外的，如果您想在本地测试，可以保留以下代码：
if __name__ == '__main__':
    # 您的配置加载和运行
    # config = load_config()
    app.run(debug=True)
# -------------------------------------------------------------
