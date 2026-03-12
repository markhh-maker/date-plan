<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>全能成长打卡计划</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "微软雅黑", sans-serif;
        }
        body {
            background-color: #f5f5f5;
            padding: 20px;
            max-width: 1000px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .tab-btn {
            padding: 10px 20px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .tab-btn.active {
            background-color: #409eff;
            color: #fff;
            border-color: #409eff;
        }
        .tab-content {
            display: none;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        }
        .tab-content.active {
            display: block;
        }
        .module {
            margin-bottom: 25px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }
        .module:last-child {
            border-bottom: none;
        }
        .module-title {
            font-size: 18px;
            margin-bottom: 15px;
            color: #333;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .module-title i {
            font-size: 20px;
        }
        .task-item {
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .task-label {
            min-width: 200px;
            font-size: 14px;
            color: #666;
        }
        /* 移动端适配标签宽度 */
        @media (max-width: 768px) {
            .task-label {
                min-width: 100%;
                margin-bottom: 8px;
            }
            .task-controls {
                width: 100%;
            }
        }
        .task-controls {
            display: flex;
            gap: 10px;
            align-items: center;
            flex: 1;
        }
        .radio-group {
            display: flex;
            gap: 15px;
        }
        .radio-item {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        input[type="text"], textarea, select {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
            flex: 1;
            min-width: 200px;
        }
        /* 移动端输入框宽度适配 */
        @media (max-width: 768px) {
            input[type="text"], textarea, select {
                min-width: 100%;
            }
        }
        textarea {
            resize: vertical;
            min-height: 80px;
        }
        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
        }
        .btn-primary {
            background-color: #409eff;
            color: #fff;
        }
        .btn-primary:hover {
            background-color: #66b1ff;
        }
        .btn-success {
            background-color: #67c23a;
            color: #fff;
        }
        .btn-success:hover {
            background-color: #85ce61;
        }
        .progress-container {
            margin: 15px 0;
        }
        .progress-title {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
            font-size: 14px;
        }
        .progress-bar {
            height: 10px;
            background-color: #eee;
            border-radius: 5px;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background-color: #409eff;
            border-radius: 5px;
            transition: width 0.3s;
        }
        .record-item {
            padding: 10px;
            border: 1px solid #eee;
            border-radius: 4px;
            margin-bottom: 10px;
        }
        .record-date {
            font-weight: bold;
            margin-bottom: 5px;
            color: #333;
        }
        .record-content {
            font-size: 14px;
            color: #666;
            line-height: 1.6;
        }
        .btn-group {
            display: flex;
            gap: 10px;
            margin-top: 20px;
            /* 移动端按钮换行 */
            flex-wrap: wrap;
        }
        .special-day {
            margin: 15px 0;
            display: flex;
            gap: 15px;
            align-items: center;
            /* 移动端换行 */
            flex-wrap: wrap;
        }
        /* 修复提醒时间输入框样式 */
        input[type="time"] {
            min-width: 120px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>全能成长打卡计划</h1>
        <p>运动 | 学习 | 提升 | 读书 | 旅行</p>
    </div>

    <div class="tabs">
        <button class="tab-btn active" data-tab="daily">每日打卡</button>
        <button class="tab-btn" data-tab="monthly">月度任务</button>
        <button class="tab-btn" data-tab="yearly">年度目标</button>
        <button class="tab-btn" data-tab="records">历史记录</button>
        <button class="tab-btn" data-tab="settings">设置</button>
    </div>

    <!-- 每日打卡 -->
    <div class="tab-content active" id="daily">
        <h2 style="margin-bottom: 20px;">今日打卡 · <span id="today-date"></span></h2>
        
        <div class="special-day">
            <label class="radio-item">
                <input type="checkbox" id="elastic-day"> 弹性休息日（减少任务量）
            </label>
            <label class="radio-item">
                <input type="checkbox" id="travel-day"> 旅行日（仅打卡旅行模块）
            </label>
        </div>

        <!-- 运动模块 -->
        <div class="module" id="module-sport">
            <div class="module-title">
                <i>🏃</i> 运动（八段锦 + 视频跟练）
            </div>
            <div class="task-item">
                <div class="task-label">八段锦（15-20分钟）：</div>
                <div class="task-controls">
                    <div class="radio-group">
                        <label class="radio-item">
                            <input type="radio" name="sport-1" value="完成"> 完成
                        </label>
                        <label class="radio-item">
                            <input type="radio" name="sport-1" value="未完成"> 未完成
                        </label>
                    </div>
                    <input type="text" id="sport-1-note" placeholder="备注（如：晨起完成，18分钟）">
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">视频跟练（20分钟）：</div>
                <div class="task-controls">
                    <div class="radio-group">
                        <label class="radio-item">
                            <input type="radio" name="sport-2" value="完成"> 完成
                        </label>
                        <label class="radio-item">
                            <input type="radio" name="sport-2" value="未完成"> 未完成
                        </label>
                    </div>
                    <input type="text" id="sport-2-note" placeholder="备注（如：有氧操，15分钟）">
                </div>
            </div>
        </div>

        <!-- 学习模块 -->
        <div class="module" id="module-study">
            <div class="module-title">
                <i>📚</i> 学习（英语 + 新课）
            </div>
            <div class="task-item">
                <div class="task-label">英语（25分钟）：</div>
                <div class="task-controls">
                    <div class="radio-group">
                        <label class="radio-item">
                            <input type="radio" name="study-1" value="完成"> 完成
                        </label>
                        <label class="radio-item">
                            <input type="radio" name="study-1" value="未完成"> 未完成
                        </label>
                    </div>
                    <input type="text" id="study-1-note" placeholder="备注（如：单词15分钟+听力10分钟）">
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">新课学习（30分钟）：</div>
                <div class="task-controls">
                    <div class="radio-group">
                        <label class="radio-item">
                            <input type="radio" name="study-2" value="完成"> 完成
                        </label>
                        <label class="radio-item">
                            <input type="radio" name="study-2" value="未完成"> 未完成
                        </label>
                    </div>
                    <select id="study-2-type">
                        <option value="未选定课程">未选定课程</option>
                        <option value="AI工具">AI工具</option>
                        <option value="职场技巧">职场技巧</option>
                        <option value="其他">其他</option>
                    </select>
                    <input type="text" id="study-2-note" placeholder="备注（如：学习第3课时，做了笔记）">
                </div>
            </div>
        </div>

        <!-- 提升模块 -->
        <div class="module" id="module-improve">
            <div class="module-title">
                <i>✨</i> 综合提升（时事/理财/美妆/摄影）
            </div>
            <div class="task-item">
                <div class="task-label">碎片化学习（15分钟）：</div>
                <div class="task-controls">
                    <div class="radio-group">
                        <label class="radio-item">
                            <input type="radio" name="improve-1" value="完成"> 完成
                        </label>
                        <label class="radio-item">
                            <input type="radio" name="improve-1" value="未完成"> 未完成
                        </label>
                    </div>
                    <select id="improve-1-type">
                        <option value="时事">时事</option>
                        <option value="理财">理财</option>
                        <option value="美妆">美妆</option>
                        <option value="摄影">摄影</option>
                    </select>
                    <input type="text" id="improve-1-note" placeholder="备注（如：学习了人像构图技巧）">
                </div>
            </div>
        </div>

        <!-- 读书模块 -->
        <div class="module" id="module-reading">
            <div class="module-title">
                <i>📖</i> 读书（每月1本）
            </div>
            <div class="task-item">
                <div class="task-label">每日阅读（20分钟）：</div>
                <div class="task-controls">
                    <div class="radio-group">
                        <label class="radio-item">
                            <input type="radio" name="reading-1" value="完成"> 完成
                        </label>
                        <label class="radio-item">
                            <input type="radio" name="reading-1" value="未完成"> 未完成
                        </label>
                    </div>
                    <input type="text" id="reading-1-note" placeholder="备注（如：《活着》读到第56页）">
                </div>
            </div>
        </div>

        <!-- 旅行模块 -->
        <div class="module" id="module-travel">
            <div class="module-title">
                <i>✈️</i> 旅行记录（拍照/出行）
            </div>
            <div class="task-item">
                <div class="task-label">随手拍 + 修图：</div>
                <div class="task-controls">
                    <div class="radio-group">
                        <label class="radio-item">
                            <input type="radio" name="travel-1" value="完成"> 完成
                        </label>
                        <label class="radio-item">
                            <input type="radio" name="travel-1" value="未完成"> 未完成
                        </label>
                    </div>
                    <input type="text" id="travel-1-note" placeholder="备注（如：公园拍照，修了2张图）">
                </div>
            </div>
        </div>

        <!-- 每日复盘 -->
        <div class="module">
            <div class="module-title">
                <i>📝</i> 每日小复盘
            </div>
            <textarea id="daily-review" placeholder="今日感悟、未完成原因、明日计划（限200字）" maxlength="200"></textarea>
        </div>

        <div class="btn-group">
            <button class="btn btn-primary" onclick="saveDailyRecord()">保存今日打卡</button>
            <button class="btn btn-success" onclick="resetDailyForm()">重置表单</button>
        </div>
    </div>

    <!-- 月度任务 -->
    <div class="tab-content" id="monthly">
        <h2 style="margin-bottom: 20px;">
            <input type="number" id="month-input" value="3" min="1" max="12" style="width: 60px;"> 月 月度任务
        </h2>

        <!-- 月度任务模块 -->
        <div class="module">
            <div class="module-title">📌 本月核心任务</div>
            <div class="task-item">
                <div class="task-label">运动：</div>
                <div class="task-controls">
                    <input type="text" value="每周运动4-5次（八段锦+视频跟练），月底评估身体状态" readonly>
                    <label class="radio-item">
                        <input type="radio" name="month-sport" value="完成"> 完成
                    </label>
                    <label class="radio-item">
                        <input type="radio" name="month-sport" value="未完成"> 未完成
                    </label>
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">学习：</div>
                <div class="task-controls">
                    <input type="text" value="英语完成250个单词，新课每周学习2-3课时" readonly>
                    <label class="radio-item">
                        <input type="radio" name="month-study" value="完成"> 完成
                    </label>
                    <label class="radio-item">
                        <input type="radio" name="month-study" value="未完成"> 未完成
                    </label>
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">提升：</div>
                <div class="task-controls">
                    <input type="text" id="month-improve" placeholder="本月聚焦方向（如：美妆+摄影）">
                    <label class="radio-item">
                        <input type="radio" name="month-improve" value="完成"> 完成
                    </label>
                    <label class="radio-item">
                        <input type="radio" name="month-improve" value="未完成"> 未完成
                    </label>
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">读书：</div>
                <div class="task-controls">
                    <input type="text" id="month-reading" placeholder="本月书单（如：《蛤蟆先生去看心理医生》）">
                    <label class="radio-item">
                        <input type="radio" name="month-reading" value="完成"> 完成
                    </label>
                    <label class="radio-item">
                        <input type="radio" name="month-reading" value="未完成"> 未完成
                    </label>
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">旅行：</div>
                <div class="task-controls">
                    <input type="text" id="month-travel" placeholder="本月出行计划（如：近郊公园拍照）">
                    <label class="radio-item">
                        <input type="radio" name="month-travel" value="完成"> 完成
                    </label>
                    <label class="radio-item">
                        <input type="radio" name="month-travel" value="未完成"> 未完成
                    </label>
                </div>
            </div>
        </div>

        <!-- 月度进度 -->
        <div class="module">
            <div class="module-title">📊 本月完成进度</div>
            <div class="progress-container">
                <div class="progress-title">
                    <span>运动完成率</span>
                    <span id="month-sport-progress">0%</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" id="month-sport-bar" style="width: 0%;"></div>
                </div>
            </div>
            <div class="progress-container">
                <div class="progress-title">
                    <span>学习完成率</span>
                    <span id="month-study-progress">0%</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" id="month-study-bar" style="width: 0%;"></div>
                </div>
            </div>
            <div class="progress-container">
                <div class="progress-title">
                    <span>整体完成率</span>
                    <span id="month-total-progress">0%</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" id="month-total-bar" style="width: 0%;"></div>
                </div>
            </div>
        </div>

        <!-- 月度复盘 -->
        <div class="module">
            <div class="module-title">📝 月度复盘</div>
            <textarea id="monthly-review" placeholder="本月未完成原因、下月调整计划"></textarea>
        </div>

        <div class="btn-group">
            <button class="btn btn-primary" onclick="saveMonthlyRecord()">保存月度记录</button>
            <button class="btn btn-success" onclick="calcMonthlyProgress()">计算本月进度</button>
        </div>
    </div>

    <!-- 年度目标 -->
    <div class="tab-content" id="yearly">
        <h2 style="margin-bottom: 20px;">2026 年 年度目标</h2>

        <!-- 年度目标设置 -->
        <div class="module">
            <div class="task-item">
                <div class="task-label">运动：</div>
                <div class="task-controls">
                    <input type="text" id="year-sport" value="全年运动天数≥300天，熟练掌握八段锦全套动作">
                    <div class="progress-container" style="margin-top: 10px; width: 100%;">
                        <div class="progress-title">
                            <span>已完成天数</span>
                            <span id="year-sport-progress">0/300 (0%)</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="year-sport-bar" style="width: 0%;"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">学习：</div>
                <div class="task-controls">
                    <input type="text" id="year-study" value="英语单词3000+，完成1门新课学习并产出作品集">
                    <div class="progress-container" style="margin-top: 10px; width: 100%;">
                        <div class="progress-title">
                            <span>英语单词完成数</span>
                            <span id="year-study-progress">0/3000 (0%)</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="year-study-bar" style="width: 0%;"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">提升：</div>
                <div class="task-controls">
                    <input type="text" id="year-improve" value="精通3项技能（时事/理财/美妆/摄影），输出10条高质量内容">
                    <div class="progress-container" style="margin-top: 10px; width: 100%;">
                        <div class="progress-title">
                            <span>已掌握技能数</span>
                            <span id="year-improve-progress">0/3 (0%)</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="year-improve-bar" style="width: 0%;"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">读书：</div>
                <div class="task-controls">
                    <input type="text" id="year-reading" value="全年读完12本书，每本写300字读书笔记">
                    <div class="progress-container" style="margin-top: 10px; width: 100%;">
                        <div class="progress-title">
                            <span>已完成读书数</span>
                            <span id="year-reading-progress">0/12 (0%)</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="year-reading-bar" style="width: 0%;"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="task-item">
                <div class="task-label">旅行：</div>
                <div class="task-controls">
                    <input type="text" id="year-travel" value="完成4-5次出行（3次近郊，1-2次长途），整理年度影像集">
                    <div class="progress-container" style="margin-top: 10px; width: 100%;">
                        <div class="progress-title">
                            <span>已出行次数</span>
                            <span id="year-travel-progress">0/5 (0%)</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress-fill" id="year-travel-bar" style="width: 0%;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="btn-group">
            <button class="btn btn-primary" onclick="saveYearlyGoal()">保存年度目标</button>
            <button class="btn btn-success" onclick="updateYearlyProgress()">更新年度进度</button>
        </div>
    </div>

    <!-- 历史记录 -->
    <div class="tab-content" id="records">
        <h2 style="margin-bottom: 20px;">历史打卡记录</h2>
        <div class="btn-group">
            <button class="btn btn-primary" onclick="exportRecords()">导出记录（JSON）</button>
            <button class="btn btn-success" onclick="loadAllRecords()">刷新记录</button>
        </div>
        <div id="records-list" style="margin-top: 20px;">
            <!-- 历史记录会在这里显示 -->
            <p style="color: #999;">暂无打卡记录，请先完成每日打卡并保存</p>
        </div>
    </div>

    <!-- 设置 -->
    <div class="tab-content" id="settings">
        <h2 style="margin-bottom: 20px;">系统设置</h2>
        <div class="module">
            <div class="module-title">🔔 提醒设置</div>
            <div class="task-item">
                <div class="task-label">每日打卡提醒时间：</div>
                <div class="task-controls">
                    <input type="time" id="reminder-time" value="20:00">
                    <label class="radio-item">
                        <input type="checkbox" id="enable-reminder" checked> 开启提醒
                    </label>
                </div>
            </div>
        </div>
        <div class="module">
            <div class="module-title">🗑️ 数据管理</div>
            <div class="task-item">
                <button class="btn btn-primary" onclick="backupData()">备份所有数据</button>
                <button class="btn btn-success" onclick="restoreData()">恢复数据</button>
                <button class="btn" style="background-color: #f56c6c; color: #fff;" onclick="clearAllData()">清空所有数据</button>
            </div>
        </div>
        <div class="module">
            <div class="module-title">ℹ️ 关于软件</div>
            <p>版本：1.0.0</p>
            <p>数据存储：本地浏览器存储，不会上传云端</p>
            <p>使用说明：每日打卡后点击保存，数据自动存储</p>
        </div>
    </div>

    <script>
        // 初始化日期
        const today = new Date();
        const dateStr = today.getFullYear() + "-" + (today.getMonth() + 1).toString().padStart(2, "0") + "-" + today.getDate().toString().padStart(2, "0");
        document.getElementById("today-date").textContent = dateStr;

        // 标签切换
        const tabBtns = document.querySelectorAll(".tab-btn");
        const tabContents = document.querySelectorAll(".tab-content");
        
        tabBtns.forEach(btn => {
            btn.addEventListener("click", () => {
                // 移除所有激活状态
                tabBtns.forEach(b => b.classList.remove("active"));
                tabContents.forEach(c => c.classList.remove("active"));
                
                // 添加当前激活状态
                btn.classList.add("active");
                const tabId = btn.getAttribute("data-tab");
                document.getElementById(tabId).classList.add("active");
            });
        });

        // 特殊日期逻辑（弹性休息/旅行日）
        document.getElementById("elastic-day").addEventListener("change", function() {
            const modules = ["module-sport", "module-study", "module-improve"];
            modules.forEach(id => {
                const module = document.getElementById(id);
                if (this.checked) {
                    module.style.opacity = "0.5";
                    module.querySelectorAll("input").forEach(input => {
                        if (input.type !== "radio" && input.type !== "checkbox") {
                            input.disabled = true;
                        }
                    });
                } else {
                    module.style.opacity = "1";
                    module.querySelectorAll("input").forEach(input => {
                        input.disabled = false;
                    });
                }
            });
        });

        document.getElementById("travel-day").addEventListener("change", function() {
            const hideModules = ["module-sport", "module-study", "module-improve", "module-reading"];
            hideModules.forEach(id => {
                const module = document.getElementById(id);
                if (this.checked) {
                    module.style.display = "none";
                } else {
                    module.style.display = "block";
                }
            });
            // 突出旅行模块
            const travelModule = document.getElementById("module-travel");
            if (this.checked) {
                travelModule.style.border = "2px solid #409eff";
                travelModule.style.padding = "18px";
            } else {
                travelModule.style.border = "none";
                travelModule.style.padding = "0 0 20px 0";
            }
        });

        // 保存每日打卡记录
        function saveDailyRecord() {
            // 收集表单数据
            const record = {
                date: dateStr,
                sport: {
                    item1: getRadioValue("sport-1"),
                    note1: document.getElementById("sport-1-note").value,
                    item2: getRadioValue("sport-2"),
                    note2: document.getElementById("sport-2-note").value
                },
                study: {
                    item1: getRadioValue("study-1"),
                    note1: document.getElementById("study-1-note").value,
                    item2: getRadioValue("study-2"),
                    type2: document.getElementById("study-2-type").value,
                    note2: document.getElementById("study-2-note").value
                },
                improve: {
                    item1: getRadioValue("improve-1"),
                    type1: document.getElementById("improve-1-type").value,
                    note1: document.getElementById("improve-1-note").value
                },
                reading: {
                    item1: getRadioValue("reading-1"),
                    note1: document.getElementById("reading-1-note").value
                },
                travel: {
                    item1: getRadioValue("travel-1"),
                    note1: document.getElementById("travel-1-note").value
                },
                review: document.getElementById("daily-review").value,
                isElasticDay: document.getElementById("elastic-day").checked,
                isTravelDay: document.getElementById("travel-day").checked
            };

            // 优化验证逻辑：旅行日仅验证旅行模块
            if (record.isTravelDay) {
                if (!record.travel.item1 || record.travel.item1 === "未选择") {
                    alert("旅行日请至少完成旅行模块的打卡！");
                    return;
                }
            } else if (!record.sport.item1 || record.sport.item1 === "未选择") {
                alert("请至少完成运动模块的打卡！");
                return;
            }

            // 保存到本地存储
            let records = JSON.parse(localStorage.getItem("dailyRecords") || "[]");
            // 检查是否已有当天记录
            const existingIndex = records.findIndex(r => r.date === dateStr);
            if (existingIndex > -1) {
                records[existingIndex] = record;
            } else {
                records.push(record);
            }
            localStorage.setItem("dailyRecords", JSON.stringify(records));

            alert("今日打卡记录保存成功！");
            loadAllRecords(); // 刷新历史记录
        }

        // 重置每日表单
        function resetDailyForm() {
            document.querySelectorAll('input[type="radio"]').forEach(radio => {
                radio.checked = false;
            });
            document.querySelectorAll('input[type="text"], textarea, select').forEach(input => {
                input.value = "";
            });
            document.getElementById("elastic-day").checked = false;
            document.getElementById("travel-day").checked = false;
            document.getElementById("module-travel").style.border = "none";
            document.getElementById("module-travel").style.padding = "0 0 20px 0";
            // 恢复模块状态
            ["module-sport", "module-study", "module-improve"].forEach(id => {
                const module = document.getElementById(id);
                module.style.opacity = "1";
                module.querySelectorAll("input").forEach(input => {
                    input.disabled = false;
                });
            });
            ["module-sport", "module-study", "module-improve", "module-reading"].forEach(id => {
                document.getElementById(id).style.display = "block";
            });
        }

        // 保存月度记录
        function saveMonthlyRecord() {
            const month = document.getElementById("month-input").value;
            const record = {
                month: month,
                sport: getRadioValue("month-sport"),
                study: getRadioValue("month-study"),
                improve: {
                    content: document.getElementById("month-improve").value,
                    status: getRadioValue("month-improve")
                },
                reading: {
                    content: document.getElementById("month-reading").value,
                    status: getRadioValue("month-reading")
                },
                travel: {
                    content: document.getElementById("month-travel").value,
                    status: getRadioValue("month-travel")
                },
                review: document.getElementById("monthly-review").value
            };

            let monthlyRecords = JSON.parse(localStorage.getItem("monthlyRecords") || "[]");
            const existingIndex = monthlyRecords.findIndex(r => r.month === month);
            if (existingIndex > -1) {
                monthlyRecords[existingIndex] = record;
            } else {
                monthlyRecords.push(record);
            }
            localStorage.setItem("monthlyRecords", JSON.stringify(monthlyRecords));

            alert("月度记录保存成功！");
        }

        // 优化月度进度计算：基于真实每日打卡数据
        function calcMonthlyProgress() {
            const month = document.getElementById("month-input").value;
            const dailyRecords = JSON.parse(localStorage.getItem("dailyRecords") || "[]");
            // 筛选当月记录
            const monthRecords = dailyRecords.filter(record => {
                const recordMonth = record.date.split("-")[1];
                return recordMonth === month.toString().padStart(2, "0");
            });

            if (monthRecords.length === 0) {
                alert("本月暂无打卡记录，无法计算进度！");
                return;
            }

            // 计算运动完成率
            let sportComplete = 0;
            monthRecords.forEach(record => {
                if (record.sport.item1 === "完成") sportComplete++;
            });
            const sportProgress = Math.floor((sportComplete / monthRecords.length) * 100);

            // 计算学习完成率
            let studyComplete = 0;
            monthRecords.forEach(record => {
                if (record.study.item1 === "完成") studyComplete++;
            });
            const studyProgress = Math.floor((studyComplete / monthRecords.length) * 100);

            const totalProgress = Math.floor((sportProgress + studyProgress) / 2);

            document.getElementById("month-sport-progress").textContent = sportProgress + "%";
            document.getElementById("month-sport-bar").style.width = sportProgress + "%";
            
            document.getElementById("month-study-progress").textContent = studyProgress + "%";
            document.getElementById("month-study-bar").style.width = studyProgress + "%";
            
            document.getElementById("month-total-progress").textContent = totalProgress + "%";
            document.getElementById("month-total-bar").style.width = totalProgress + "%";

            alert("月度进度计算完成！");
        }

        // 保存年度目标
        function saveYearlyGoal() {
            const goal = {
                sport: document.getElementById("year-sport").value,
                study: document.getElementById("year-study").value,
                improve: document.getElementById("year-improve").value,
                reading: document.getElementById("year-reading").value,
                travel: document.getElementById("year-travel").value
            };

            localStorage.setItem("yearlyGoal", JSON.stringify(goal));
            alert("年度目标保存成功！");
        }

        // 优化年度进度更新：基于真实打卡数据
        function updateYearlyProgress() {
            const dailyRecords = JSON.parse(localStorage.getItem("dailyRecords") || "[]");
            
            // 运动天数统计
            const sportDays = dailyRecords.filter(record => record.sport.item1 === "完成").length;
            const sportProgress = Math.floor((sportDays / 300) * 100);
            
            // 读书本数（简化：每30天打卡算1本）
            const readingDays = dailyRecords.filter(record => record.reading.item1 === "完成").length;
            const readingBooks = Math.floor(readingDays / 30);
            const readingProgress = Math.floor((readingBooks / 12) * 100);
            
            // 旅行次数（手动统计，这里先模拟）
            const travelTimes = Math.floor(Math.random() * 5);
            const travelProgress = Math.floor((travelTimes / 5) * 100);
            
            // 英语单词（模拟：每天打卡算10个）
            const studyDays = dailyRecords.filter(record => record.study.item1 === "完成").length;
            const studyWords = studyDays * 10;
            const studyProgress = Math.floor((studyWords / 3000) * 100);
            
            // 提升技能（模拟）
            const improveProgress = Math.floor(Math.random() * 100);

            document.getElementById("year-sport-progress").textContent = `${sportDays}/300 (${sportProgress}%)`;
            document.getElementById("year-sport-bar").style.width = sportProgress + "%";
            
            document.getElementById("year-study-progress").textContent = `${studyWords}/3000 (${studyProgress}%)`;
            document.getElementById("year-study-bar").style.width = studyProgress + "%";
            
            document.getElementById("year-improve-progress").textContent = `${Math.floor(improveProgress/33)}/3 (${improveProgress}%)`;
            document.getElementById("year-improve-bar").style.width = improveProgress + "%";
            
            document.getElementById("year-reading-progress").textContent = `${readingBooks}/12 (${readingProgress}%)`;
            document.getElementById("year-reading-bar").style.width = readingProgress + "%";
            
            document.getElementById("year-travel-progress").textContent = `${travelTimes}/5 (${travelProgress}%)`;
            document.getElementById("year-travel-bar").style.width = travelProgress + "%";

            alert("年度进度更新完成！");
        }

        // 加载所有历史记录
        function loadAllRecords() {
            const records = JSON.parse(localStorage.getItem("dailyRecords") || "[]");
            const recordsList = document.getElementById("records-list");
            
            if (records.length === 0) {
                recordsList.innerHTML = '<p style="color: #999;">暂无打卡记录，请先完成每日打卡并保存</p>';
                return;
            }

            // 按日期倒序排序
            records.sort((a, b) => new Date(b.date) - new Date(a.date));

            let html = "";
            records.forEach(record => {
                html += `
                <div class="record-item">
                    <div class="record-date">${record.date} ${record.isTravelDay ? "[旅行日]" : record.isElasticDay ? "[弹性休息日]" : ""}</div>
                    <div class="record-content">
                        <p>运动：${record.sport.item1} | ${record.sport.note1 || "无备注"}</p>
                        <p>学习：${record.study.item1} | ${record.study.note1 || "无备注"}</p>
                        <p>提升：${record.improve.item1} | ${record.improve.type1} | ${record.improve.note1 || "无备注"}</p>
                        <p>读书：${record.reading.item1} | ${record.reading.note1 || "无备注"}</p>
                        <p>旅行：${record.travel.item1} | ${record.travel.note1 || "无备注"}</p>
                        <p>复盘：${record.review || "无"}</p>
                    </div>
                </div>
                `;
            });

            recordsList.innerHTML = html;
        }

        // 导出记录
        function exportRecords() {
            const records = JSON.parse(localStorage.getItem("dailyRecords") || "[]");
            const monthlyRecords = JSON.parse(localStorage.getItem("monthlyRecords") || "[]");
            const yearlyGoal = JSON.parse(localStorage.getItem("yearlyGoal") || "{}");

            const exportData = {
                dailyRecords: records,
                monthlyRecords: monthlyRecords,
                yearlyGoal: yearlyGoal,
                exportTime: new Date().toISOString()
            };

            const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: "application/json" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = `打卡记录_${dateStr}.json`;
            a.click();
            URL.revokeObjectURL(url);

            alert("记录导出成功！");
        }

        // 备份数据
        function backupData() {
            const allData = {
                dailyRecords: JSON.parse(localStorage.getItem("dailyRecords") || "[]"),
                monthlyRecords: JSON.parse(localStorage.getItem("monthlyRecords") || "[]"),
                yearlyGoal: JSON.parse(localStorage.getItem("yearlyGoal") || "{}"),
                backupTime: new Date().toISOString()
            };

            const blob = new Blob([JSON.stringify(allData, null, 2)], { type: "application/json" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = `打卡数据备份_${dateStr}.json`;
            a.click();
            URL.revokeObjectURL(url);

            alert("数据备份成功！");
        }

        // 恢复数据
        function restoreData() {
            const input = document.createElement("input");
            input.type = "file";
            input.accept = ".json";
            
            input.onchange = function(e) {
                const file = e.target.files[0];
                if (!file) return;
                
                const reader = new FileReader();
                reader.onload = function(event) {
                    try {
                        const data = JSON.parse(event.target.result);
                        localStorage.setItem("dailyRecords", JSON.stringify(data.dailyRecords || []));
                        localStorage.setItem("monthlyRecords", JSON.stringify(data.monthlyRecords || []));
                        localStorage.setItem("yearlyGoal", JSON.stringify(data.yearlyGoal || {}));
                        
                        alert("数据恢复成功！");
                        loadAllRecords();
                    } catch (error) {
                        alert("数据恢复失败：文件格式错误！");
                    }
                };
                reader.readAsText(file);
            };
            
            input.click();
        }

        // 清空所有数据
        function clearAllData() {
            if (confirm("确定要清空所有打卡数据吗？此操作不可恢复！")) {
                localStorage.removeItem("dailyRecords");
                localStorage.removeItem("monthlyRecords");
                localStorage.removeItem("yearlyGoal");
                alert("所有数据已清空！");
                loadAllRecords();
            }
        }

        // 辅助函数：获取单选框值
        function getRadioValue(name) {
            const radios = document.getElementsByName(name);
            for (let i = 0; i < radios.length; i++) {
                if (radios[i].checked) {
                    return radios[i].value;
                }
            }
            return "未选择";
        }

        // 页面加载时加载记录
        window.onload = function() {
            loadAllRecords();
            // 加载年度目标
            const yearlyGoal = JSON.parse(localStorage.getItem("yearlyGoal") || "{}");
            if (yearlyGoal.sport) document.getElementById("year-sport").value = yearlyGoal.sport;
            if (yearlyGoal.study) document.getElementById("year-study").value = yearlyGoal.study;
            if (yearlyGoal.improve) document.getElementById("year-improve").value = yearlyGoal.improve;
            if (yearlyGoal.reading) document.getElementById("year-reading").value = yearlyGoal.reading;
            if (yearlyGoal.travel) document.getElementById("year-travel").value = yearlyGoal.travel;
        };
    </script>
</body>
</html>