// 示例 JSON 数据
const jsonData = {
    "name": "Root",
    "children": [
        {
            "name": "Child 1",
            "children": [
                {"name": "Grandchild 1.1"},
                {"name": "Grandchild 1.2"}
            ]
        },
        {"name": "Child 2"},
        {
            "name": "Child 3",
            "children": [
                {"name": "Grandchild 3.1", "special": true},
                {"name": "Grandchild 3.2"},
                {"name": "Grandchild 3.3"}
            ]
        }
    ]
};

// 递归生成树形结构的函数
function generateTree(data, parent) {
    const ul = document.createElement('ul');
    ul.classList.add('tree');
    parent.appendChild(ul);
    data.forEach(item => {
        const li = document.createElement('li');
        const span = document.createElement('span');
        span.classList.add('tree-node');
        span.textContent = item.name;
        li.appendChild(span);
        ul.appendChild(li);
        if (item.children && item.children.length > 0) {
            const childrenDiv = document.createElement('div');
            childrenDiv.classList.add('tree-children');
            li.appendChild(childrenDiv);
            generateTree(item.children, childrenDiv);
            span.classList.add('expanded');
        }
    });
}

// 优化后的节点点击事件处理函数
function handleNodeClick(event) {
    const node = event.target.closest('.tree-node');
    if (!node) return;
    const childrenDiv = node.nextElementSibling;
    if (childrenDiv && childrenDiv.classList.contains('tree-children')) {
        node.classList.toggle('expanded');
        childrenDiv.classList.toggle('expanded');
    }
}

// 处理键盘事件
function handleKeyDown(event) {
    const focusedNode = document.activeElement.closest('.tree-node');
    if (!focusedNode) return;
    const nodes = Array.from(document.querySelectorAll('.tree-node'));
    const index = nodes.indexOf(focusedNode);
    switch (event.key) {
        case 'ArrowDown':
            event.preventDefault();
            if (index < nodes.length - 1) {
                nodes[index + 1].focus();
            }
            break;
        case 'ArrowUp':
            event.preventDefault();
            if (index > 0) {
                nodes[index - 1].focus();
            }
            break;
        case 'ArrowLeft':
            event.preventDefault();
            if (focusedNode.classList.contains('expanded')) {
                handleNodeClick({ target: focusedNode });
            }
            break;
        case 'ArrowRight':
            event.preventDefault();
            if (focusedNode.classList.contains('collapsed')) {
                handleNodeClick({ target: focusedNode });
            }
            break;
    }
}

// 页面加载时初始化树形结构和事件绑定
window.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('tree-container');
    generateTree([jsonData], container);
    container.addEventListener('click', (event) => {
        if (event.target.closest('.tree-node')) {
            handleNodeClick(event);
        }
    });
    container.addEventListener('keydown', handleKeyDown);
});