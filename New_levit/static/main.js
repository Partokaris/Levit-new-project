function increment(){
    console.log("increment")
}
function decrement(){
    console.log("decrement")
}
function update(){
    console.log("decrement")
}
document.addEventListener("DOMContentLoaded", () => {
    const showCartButton = document.getElementById("show-cart");
    const cartCard = document.querySelector(".cart-card");
    const cartOverlay = document.getElementById("cart-overlay");

   

    var AddToCart= document.getElementsByClassName('add-to-cart')
    console.log(AddToCart)
    for (var i=0; i<AddToCart.length;i++){
        button=AddToCart[i]
        button.addEventListener('click',Addtocart)

    }

    function Addtocart(event){
        var button= event.target
        var shopitem=button.parentElement.parentElement
        var title=shopitem.getElementsByClassName('card-title')[0].innerText
        var price=shopitem.getElementsByClassName('card-price')[0].innerText
        var image=shopitem.getElementsByClassName('card-img-top')[0].src
        var Description=shopitem.getElementsByClassName('card-text')[0].innerText
        console.log(title, price,image, Description)
        additemtocart(image,title,Description,price)
    }
    
    function additemtocart(image, title, Description, price){
        cartrow=document.createElement('div')
        var cartitems=document.getElementsByClassName('cart-item')[0]
        var cartitemcontent=`
        <div class="row cart-item border-top border-bottom">
            <div class="row main align-items-center">
                <img class="img-fluid" src="${image}">
                <div class="col">
                    <div class="row">${title}</div>
                </div>
                <div class="buttons">
                    <i onclick="increment()" class="bi bi-plus-lg"></i>
                    <div id=&{id} class="quantity">0</div>
                    <i onclick="decrement()" class="bi bi-dash-lg"></i>
                </div>
                <div class="col">&euro; ${price} <span class="close">&#10005;</span></div>
            </div>
        </div>`
        cartrow.innerHTML=cartitemcontent
        cartitems.append(cartrow)
    }
    
});
