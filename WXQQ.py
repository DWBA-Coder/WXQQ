import os
import sys
import ctypes
import subprocess

# 定义应用路径
WEIXIN_PATH = r"D:\Program Files\Tencent\Weixin\Weixin.exe"
QQ_PATH = r"D:\Program Files\Tencent\QQNT\QQ.exe"

def launch_app(path, name):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"{name}路径不存在: {path}")

        # Windows专有方法：使用ShellExecute启动完全独立的进程
        ctypes.windll.shell32.ShellExecuteW(
            None,               # 父窗口句柄
            "open",             # 操作方式
            path,               # 程序路径
            None,               # 参数
            None,               # 工作目录
            1                   # 窗口显示方式 (1=正常窗口)
        )

    except Exception as e:
        ctypes.windll.user32.MessageBoxW(
            0,
            f"启动{name}失败: {str(e)}",
            "启动错误",
            0x10  # 错误图标
        )
        sys.exit(1)

if __name__ == "__main__":
    # 启动微信（独立进程）
    launch_app(WEIXIN_PATH, "微信")

    # 启动QQ（独立进程）
    launch_app(QQ_PATH, "QQ")

    # 立即退出脚本
    sys.exit(0)
