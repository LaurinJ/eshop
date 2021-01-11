var updateBtns = document.getElementsByClassName('update-cart');
  console.log(user);

  for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function () {
      var productId = this.dataset.product;
      var action = this.dataset.action;
      var quantity = document.getElementById('id_quantity').value;
      console.log('productId:', productId, 'Action:', action, 'quantity:', quantity);

      if (user == 'AnonymousUser'){
          console.log('AnonymousUser');
      }else{
          updateUserOrder(productId, action, quantity);
      }

    })



  }

function updateUserOrder(productId, action, quantity) {
    console.log('Update')

    var url = '/cart/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action, 'quantity':quantity})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log(data)
            location.reload()
        })
    }