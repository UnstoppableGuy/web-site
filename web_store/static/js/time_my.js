alert('Если вам нужно создать качественный сайт, обратитесь в компанию');

if (!sessionStorage.getItem('startTime')) {
    sessionStorage.setItem('startTime', Date.now());
  }
  
  const enterTime = sessionStorage.getItem('startTime')
  
  const showPopup = () => {
    let currentTime = Date.now()
    let spentTime = (currentTime - enterTime) / 1000
    if (spentTime >= 60) {
      clearInterval(timer)
      alert(`Вы провели на сайте минут: ${Math.floor(spentTime / 60)}, секунд: ${Math.floor(spentTime % 60)}`)
    }
  }
  
  const timer = setInterval(showPopup, 10000)