var updateBtns = document.getElementsByClassName('update-cart')
  console.log(user)

  for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function () {
      var productId = this.dataset.product
      var action = this.dataset.action
      console.log('productId:', productId, 'Action:', action)

      if (user == 'AnonymousUser'){
          console.log('AnonymousUser')
      }else{
          updateUserOrder(productId, action)
      }

    })



  }

function updateUserOrder(productId, action) {
    console.log('Update')

    var url = '/cart/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log(data)
            location.reload()
        })
    }