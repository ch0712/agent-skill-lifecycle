from setuptools import setup, find_packages

setup(
    name="skill-protocol",
    version="0.1.0",
    description="Agent Skill Lifecycle Protocol — 让AI Agent在使用中自主进化的技能协议与生命周期方法论",
    author="Zi Ye (子冶)",
    author_email="",
    url="https://gitee.com/xumijie/agent-skill-lifecycle",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    python_requires=">=3.9",
    install_requires=[
        "pyyaml>=6.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "pytest-cov>=4.0"],
    },
    entry_points={
        "console_scripts": [
            "skill-protocol=skill_protocol.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
