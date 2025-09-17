# 航空旅客流量分析项目 ✈️

本项目收集并整理了中国的航空旅客吞吐量数据，数据来源于中国交通部民航数据，时间范围为 **2013年1月至2025年7月**。项目旨在帮助研究者和爱好者更好地理解中国民航客运的发展趋势。

## 📂 仓库结构
airport-passenger-analysis/
├── data/ # CSV 数据文件
│ └── airport_passengers.csv
├── scripts/ # Python 脚本
│ └── analysis.py
├── notebooks/ # Jupyter Notebook 分析
│ └── analysis.ipynb
├── figures/ # 图表输出
│ └── trends.png
├── README.md # 项目说明（当前文件）
└── requirements.txt # Python 依赖

## 📊 数据说明
- **时间范围**：2013年1月至2025年7月  
- **数据来源**：中国交通部民航数据  
- **字段示例**：  
  - `Year`：年份  
  - `Month`：月份  
  - `Domestic`、`HK_MO`、`INTERNATIONAL`：旅客吞吐量（万人次）  

## 🔍 分析方法
1. **阶段划分**：根据经济发展和疫情因素，将时间划分为若干阶段进行对比。  
2. **可视化**：利用 Python（pandas / matplotlib / seaborn）绘制折线图、热力图等。  

## 📈 示例结果
- 各阶段旅客吞吐量对比图  
- 前十大机场旅客量趋势  
- 热力图展示不同机场随时间的变化  

（这里可放置一张示例图，如 `figures/trends.png`）

## 📑 使用说明
克隆项目并安装依赖：

```bash
git clone https://github.com/你的用户名/airport-passenger-analysis.git
cd airport-passenger-analysis
pip install -r requirements.txt

python scripts/analysis.py

jupyter notebook notebooks/analysis.ipynb



本项目采用 MIT 许可证开源，详见 LICENSE 文件。

---

### 2️⃣ LICENSE 文件
如果你选择 MIT 许可证，需要在项目根目录新建一个 `LICENSE` 文件，内容如下（可直接复制到文件里）：

```text
MIT License

Copyright (c) 2025 你的名字或用户名

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
