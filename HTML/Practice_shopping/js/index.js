window.addEventListener('load', function () {
    // 获取左右两个跳转箭头
    var arrow_left = this.document.querySelector('.arrow_left');
    var arrow_right = this.document.querySelector('.arrow_right');
    var focus = this.document.querySelector('.focuspoint');
    focus.addEventListener('mouseover', function () {
        arrow_left.style.display = 'block';
        arrow_right.style.display = 'block';
        // 鼠标经过停止定时播放定时器
        clearInterval(timer);
        // 清除定时器变量
        timer = null;
    })
    focus.addEventListener('mouseout', function () {
        arrow_left.style.display = 'none';
        arrow_right.style.display = 'none';
        // 鼠标离开后开启自动播放定时器
        timer = setInterval(function () {
            // 模拟点击右箭头切换图片
            arrow_right.click();
        }, 2000);

    })
    var ul = focus.querySelector('ul');
    var ol = focus.querySelector('ol');
    var focusWidth = focus.offsetWidth;
    var imgNum = ul.children.length;
    var order = 0;
    var circle = 0;
    function exclusionLi() {
        // 点击当前小li时，把其他li的类名都改为空
        for (var i = 0; i < ol.children.length; i++) {
            ol.children[i].className = '';
        }
    }
    // 获取需要的小圆圈个数
    for (var i = 0; i < imgNum; i++) {
        // 创建一个小圆圈
        var li = this.document.createElement('li');
        // 通过自定义属性记录当前小圆圈的索引号
        li.setAttribute('index', i);
        ol.appendChild(li);
        // 在生成小圆圈的时候直接对校园群进行事件绑定
        li.addEventListener('mouseover', function () {
            exclusionLi();
            // 将被点击的li类名设置为current
            this.className = 'current';
            // 鼠标经过小圆圈时移动ul实现图片切换的效果
            var index = this.getAttribute('index')
            // 当鼠标经过小圆圈时就要把索引号也给order和circle，保持小圆圈和图片索引的一致性
            order = index;
            circle = index;
            moveAnimate(ul, -index * focusWidth);
        })
    }
    // 将第一个小圆圈设置类名，作为默认的小圆圈
    ol.children[0].className = 'current';
    // 克隆第一张图片li放在最后面
    var first = ul.children[0].cloneNode(true);
    ul.appendChild(first);
    // 点击右侧按钮实现图片滚动一张效果
    arrow_right.addEventListener('click', function () {
        if (order == imgNum) {
            ul.style.left = 0;
            order = 0;
        }
        order++;
        moveAnimate(ul, -order * focusWidth);
        // 设置让小圆圈跟随图片的更换而变化
        circle++;
        circleChange();
    })
    // 点击左侧按钮实现图片滚动一张效果
    arrow_left.addEventListener('click', function () {
        if (order == 0) {
            ul.style.left = -imgNum * focusWidth + 'px';
            order = imgNum;
            // circle = imgNum - 1
        }
        order--;
        moveAnimate(ul, -order * focusWidth);
        // 设置让小圆圈跟随图片的更换而变化
        circle--;
        circleChange();
    })
    function circleChange() {
        exclusionLi();
        circle = circle < 0 ? ol.children.length - 1 : circle;
        ol.children[circle % imgNum].className = 'current';
    }
    // 定时器，自动播放轮播图
    var timer = this.setInterval(function () {
        // 模拟点击右箭头切换图片
        arrow_right.click();
    }, 2000)
})