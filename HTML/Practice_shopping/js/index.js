window.addEventListener('load', function () {
    // 获取左右两个跳转箭头
    var arrow_left = this.document.querySelector('.arrow_left');
    var arrow_right = this.document.querySelector('.arrow_right');
    var focus = this.document.querySelector('.focuspoint');
    focus.addEventListener('mouseover', function () {
        arrow_left.style.display = 'block';
        arrow_right.style.display = 'block';
    })
    focus.addEventListener('mouseout', function () {
        arrow_left.style.display = 'none';
        arrow_right.style.display = 'none';
    })
    var ul = focus.querySelector('ul');
    var ol = focus.querySelector('ol');
    // 获取需要的小圆圈个数
    for (var i = 0; i < ul.children.length; i++) {
        // 创建一个小圆圈
        var li = this.document.createElement('li');
        ol.appendChild(li);
        // 在生成小圆圈的时候直接对校园群进行事件绑定
        li.addEventListener('mouseover', function () {
            // 点击当前小li时，把其他li的类名都改为空
            for (var i = 0; i < ol.children.length; i++) {
                ol.children[i].className = '';
            }
            // 将被点击的li类名设置为current
            this.className = 'current';
        })
    }
    // 将第一个小圆圈设置类名，作为默认的小圆圈
    ol.children[0].className = 'current';
    arrow_left
})