/* ========================================
 * File-Suffix-Guide 在线查询 - 逻辑脚本
 * ======================================== */

(function () {
    'use strict';

    // ========== 全局状态 ==========
    const state = {
        allData: [],           // 所有后缀数据
        filteredData: [],      // 筛选后的数据
        searchKeyword: '',     // 搜索关键词
        activeCategory: 'all', // 当前选中分类
        activeLetter: '',      // 当前选中字母
        categories: [],        // 分类列表
    };

    // DOM 元素引用
    const el = {};

    // ========== 初始化 ==========
    document.addEventListener('DOMContentLoaded', init);

    function init() {
        // 缓存 DOM 元素
        el.searchInput = document.getElementById('searchInput');
        el.clearSearch = document.getElementById('clearSearch');
        el.resultCount = document.getElementById('resultCount');
        el.alphabetBar = document.getElementById('alphabetBar');
        el.categoryFilters = document.getElementById('categoryFilters');
        el.cardsContainer = document.getElementById('cardsContainer');
        el.noResults = document.getElementById('noResults');
        el.themeToggle = document.getElementById('themeToggle');
        el.detailModal = document.getElementById('detailModal');
        el.modalClose = document.getElementById('modalClose');
        el.modalBody = document.getElementById('modalBody');

        // 初始化主题
        initTheme();

        // 加载数据
        loadData().then(() => {
            // 初始化分类
            initCategories();
            // 初始化字母索引
            initAlphabet();
            // 渲染所有卡片
            renderCards();
            // 绑定事件
            bindEvents();
        }).catch(err => {
            console.error('加载数据失败:', err);
            showLoadError();
        });
    }

    // ========== 数据加载 ==========
    function loadData() {
        return fetch('data.json', { cache: 'no-cache' })
            .then(response => {
                if (!response.ok) {
                    throw new Error('HTTP ' + response.status);
                }
                return response.json();
            })
            .then(data => {
                state.allData = data;
                state.filteredData = [...data];
                return data;
            })
            .catch(err => {
                // 如果 fetch 失败（可能是 file:// 协议限制），尝试用 XMLHttpRequest
                return new Promise((resolve, reject) => {
                    const xhr = new XMLHttpRequest();
                    xhr.open('GET', 'data.json', true);
                    xhr.onreadystatechange = function () {
                        if (xhr.readyState === 4) {
                            if (xhr.status === 0 || xhr.status === 200) {
                                try {
                                    const data = JSON.parse(xhr.responseText);
                                    state.allData = data;
                                    state.filteredData = [...data];
                                    resolve(data);
                                } catch (e) {
                                    reject(e);
                                }
                            } else {
                                reject(new Error('XMLHttpRequest 失败: ' + xhr.status));
                            }
                        }
                    };
                    xhr.onerror = () => reject(err);
                    xhr.send();
                });
            });
    }

    function showLoadError() {
        el.cardsContainer.innerHTML = '';
        el.noResults.style.display = 'block';
        el.noResults.innerHTML = `
            <div class="no-results-icon">⚠️</div>
            <p>数据加载失败</p>
            <p class="no-results-hint">
                可能是浏览器安全限制导致无法读取本地 JSON 文件<br>
                请使用以下方式之一：<br>
                1. 使用 Firefox 浏览器直接打开<br>
                2. 使用本地服务器（如 VS Code Live Server）打开<br>
                3. 检查 data.json 文件是否存在于同一目录
            </p>
        `;
        el.resultCount.textContent = '加载失败';
    }

    // ========== 分类初始化 ==========
    function initCategories() {
        // 从数据中提取所有分类（按 categoryPath 排序）
        const categoryMap = new Map();
        state.allData.forEach(item => {
            if (!categoryMap.has(item.categoryPath)) {
                categoryMap.set(item.categoryPath, item.category);
            }
        });

        // 按分类路径排序
        const sortedCategories = Array.from(categoryMap.entries())
            .sort((a, b) => a[0].localeCompare(b[0]))
            .map(([path, name]) => ({ path, name }));

        state.categories = sortedCategories;
        renderCategoryFilters();
    }

    function renderCategoryFilters() {
        let html = '<button class="category-btn active" data-category="all">全部</button>';

        state.categories.forEach(cat => {
            html += `<button class="category-btn" data-category="${cat.path}">${cat.name}</button>`;
        });

        el.categoryFilters.innerHTML = html;
    }

    // ========== 字母索引 ==========
    function initAlphabet() {
        const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
        let html = '';

        // 检查每个字母是否有对应的后缀
        const availableLetters = new Set();
        state.allData.forEach(item => {
            const firstChar = item.suffix.charAt(0).toUpperCase();
            if (/[A-Z]/.test(firstChar)) {
                availableLetters.add(firstChar);
            }
        });

        // 数字开头的归为 #
        const hasNumberPrefix = state.allData.some(item => /^[0-9]/.test(item.suffix));

        // 添加 # 号（数字开头）
        if (hasNumberPrefix) {
            html += `<span class="alphabet-letter" data-letter="#">#</span>`;
        }

        letters.forEach(letter => {
            const disabled = availableLetters.has(letter) ? '' : 'disabled';
            html += `<span class="alphabet-letter ${disabled}" data-letter="${letter}">${letter}</span>`;
        });

        el.alphabetBar.innerHTML = html;
    }

    // ========== 卡片渲染 ==========
    function renderCards() {
        const data = state.filteredData;

        if (data.length === 0) {
            el.cardsContainer.innerHTML = '';
            el.noResults.style.display = 'block';
        } else {
            el.noResults.style.display = 'none';

            const html = data.map(item => createCardHTML(item)).join('');
            el.cardsContainer.innerHTML = html;
        }

        updateResultCount();
    }

    function createCardHTML(item) {
        const tagsHTML = item.tags.slice(0, 3).map(tag =>
            `<span class="card-tag">${tag}</span>`
        ).join('');

        return `
            <div class="suffix-card" data-suffix="${item.suffix}">
                <div class="card-suffix">.${item.suffix}</div>
                <div class="card-name">${item.name}</div>
                <span class="card-category">${item.category}</span>
                <div class="card-tags">${tagsHTML}</div>
                <span class="card-detail-link">查看详情</span>
            </div>
        `;
    }

    function updateResultCount() {
        const total = state.allData.length;
        const filtered = state.filteredData.length;

        if (state.searchKeyword || state.activeCategory !== 'all' || state.activeLetter) {
            el.resultCount.textContent = `找到 ${filtered} 个后缀（共 ${total} 个）`;
        } else {
            el.resultCount.textContent = `共收录 ${total} 个文件后缀`;
        }
    }

    // ========== 搜索功能 ==========
    function handleSearch(keyword) {
        state.searchKeyword = keyword.trim().toLowerCase();
        applyFilters();
    }

    // ========== 分类筛选 ==========
    function handleCategoryFilter(categoryPath) {
        state.activeCategory = categoryPath;
        applyFilters();

        // 更新按钮状态
        document.querySelectorAll('.category-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.category === categoryPath);
        });
    }

    // ========== 字母索引 ==========
    function handleLetterFilter(letter) {
        if (state.activeLetter === letter) {
            // 再次点击取消筛选
            state.activeLetter = '';
        } else {
            state.activeLetter = letter;
        }
        applyFilters();

        // 更新字母状态
        document.querySelectorAll('.alphabet-letter').forEach(el => {
            el.classList.toggle('active', el.dataset.letter === state.activeLetter);
        });

        // 如果有匹配项，滚动到第一个
        if (state.activeLetter && state.filteredData.length > 0) {
            const firstCard = el.cardsContainer.querySelector('.suffix-card');
            if (firstCard) {
                firstCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }

    // ========== 综合筛选 ==========
    function applyFilters() {
        let result = [...state.allData];

        // 搜索筛选
        if (state.searchKeyword) {
            const kw = state.searchKeyword;
            result = result.filter(item => {
                // 搜索后缀名
                if (item.suffix.toLowerCase().includes(kw)) return true;
                // 搜索中文名
                if (item.name.toLowerCase().includes(kw)) return true;
                // 搜索分类
                if (item.category.toLowerCase().includes(kw)) return true;
                // 搜索标签
                if (item.tags.some(tag => tag.toLowerCase().includes(kw))) return true;
                return false;
            });
        }

        // 分类筛选
        if (state.activeCategory !== 'all') {
            result = result.filter(item => item.categoryPath === state.activeCategory);
        }

        // 字母筛选
        if (state.activeLetter) {
            if (state.activeLetter === '#') {
                // 数字开头
                result = result.filter(item => /^[0-9]/.test(item.suffix));
            } else {
                result = result.filter(item =>
                    item.suffix.charAt(0).toUpperCase() === state.activeLetter
                );
            }
        }

        state.filteredData = result;
        renderCards();
    }

    // ========== 详情弹窗 ==========
    function showDetail(suffixName) {
        const item = state.allData.find(d => d.suffix === suffixName);
        if (!item) return;

        const tagsHTML = item.tags.map(tag =>
            `<span class="modal-tag">${tag}</span>`
        ).join('');

        // 构建详情路径（相对路径，指向 docs 目录）
        const docLink = '../' + item.docPath;

        el.modalBody.innerHTML = `
            <div class="modal-body">
                <div class="modal-header">
                    <div class="modal-suffix">.${item.suffix}</div>
                    <div class="modal-name">${item.name}</div>
                    <span class="modal-category">${item.category}</span>
                </div>

                <div class="modal-section">
                    <div class="modal-section-title">标签</div>
                    <div class="modal-tags">${tagsHTML}</div>
                </div>

                <div class="modal-section">
                    <div class="modal-section-title">所属分类</div>
                    <div class="modal-section-content">
                        <p>${item.category}（${item.categoryPath}）</p>
                    </div>
                </div>

                <div class="modal-section">
                    <div class="modal-section-title">文档路径</div>
                    <div class="modal-section-content">
                        <code style="background: var(--bg-category); padding: 4px 8px; border-radius: 4px; font-size: 13px;">
                            ${item.docPath}
                        </code>
                    </div>
                </div>

                <div class="modal-section">
                    <a href="${docLink}" target="_blank" class="modal-doc-link">
                        📖 查看完整文档
                    </a>
                </div>
            </div>
        `;

        el.detailModal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }

    function closeDetail() {
        el.detailModal.style.display = 'none';
        document.body.style.overflow = '';
    }

    // ========== 主题切换 ==========
    function initTheme() {
        // 从本地存储读取主题设置
        const savedTheme = localStorage.getItem('fsg-theme');
        if (savedTheme) {
            setTheme(savedTheme);
        } else {
            // 检测系统主题偏好
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            setTheme(prefersDark ? 'dark' : 'light');
        }
    }

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('fsg-theme', theme);
        updateThemeIcon(theme);
    }

    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    }

    function updateThemeIcon(theme) {
        const icon = el.themeToggle.querySelector('.theme-icon');
        if (icon) {
            icon.textContent = theme === 'dark' ? '☀️' : '🌙';
        }
        el.themeToggle.title = theme === 'dark' ? '切换到亮色模式' : '切换到暗色模式';
    }

    // ========== 事件绑定 ==========
    function bindEvents() {
        // 搜索输入
        el.searchInput.addEventListener('input', function (e) {
            const value = e.target.value;
            el.clearSearch.style.display = value ? 'flex' : 'none';
            handleSearch(value);
        });

        // 清空搜索
        el.clearSearch.addEventListener('click', function () {
            el.searchInput.value = '';
            el.clearSearch.style.display = 'none';
            handleSearch('');
            el.searchInput.focus();
        });

        // 分类筛选
        el.categoryFilters.addEventListener('click', function (e) {
            const btn = e.target.closest('.category-btn');
            if (btn) {
                handleCategoryFilter(btn.dataset.category);
            }
        });

        // 字母索引
        el.alphabetBar.addEventListener('click', function (e) {
            const letterEl = e.target.closest('.alphabet-letter');
            if (letterEl && !letterEl.classList.contains('disabled')) {
                handleLetterFilter(letterEl.dataset.letter);
            }
        });

        // 卡片点击
        el.cardsContainer.addEventListener('click', function (e) {
            const card = e.target.closest('.suffix-card');
            if (card) {
                showDetail(card.dataset.suffix);
            }
        });

        // 主题切换
        el.themeToggle.addEventListener('click', toggleTheme);

        // 关闭弹窗
        el.modalClose.addEventListener('click', closeDetail);
        el.detailModal.addEventListener('click', function (e) {
            if (e.target === el.detailModal) {
                closeDetail();
            }
        });

        // ESC 键关闭弹窗
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && el.detailModal.style.display === 'flex') {
                closeDetail();
            }
        });

        // 搜索框快捷键
        document.addEventListener('keydown', function (e) {
            // Ctrl/Cmd + K 聚焦搜索框
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                el.searchInput.focus();
                el.searchInput.select();
            }
        });
    }

})();
