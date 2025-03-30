// 目前仅为简单示例，未实现实际功能交互
// 筛选按钮点击事件
document.getElementById('filter - button').addEventListener('click', function () {
    // 这里可添加实际筛选逻辑，比如获取输入框值，向服务器请求数据等
    console.log('筛选按钮被点击');
  });
  
  // 清空按钮点击事件
  document.getElementById('clear - button').addEventListener('click', function () {
    // 这里可添加清空输入框等逻辑
    console.log('清空按钮被点击');
  });
  
  // 分页链接点击事件
  const pageLinks = document.querySelectorAll('.page - link');
  pageLinks.forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      // 这里可添加实际分页逻辑，比如向服务器请求对应页码数据等
      console.log('点击了页码:', this.textContent);
    });
  });