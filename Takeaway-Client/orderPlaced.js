




function orderSaved(obj, item){
    debugger;
    var postData = {
        name: obj.name,
        postid: obj.id,
        description:obj.description,
        brand:obj.brand,
        price:obj.price
      };
      
      // Make a POST request with the Fetch API
      fetch('http://localhost:1222/add-order', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData) // Convert the data to JSON string
      })
      .then(response => response.json()) 
      .then(data => {
        console.log(data);
        document.cookie = "orderId="+0 +",counter="+0
      })
      .catch(error => {
        console.error('Error:', error);
      });

}
let httpRequest = new XMLHttpRequest()
let totalAmount = 0
httpRequest.onreadystatechange = function()
{
    if(this.readyState === 4)
    {
        if(this.status == 200)
        {
            // console.log('call successful');
            contentTitle = JSON.parse(this.responseText)

            let counter = Number(document.cookie.split(',')[1].split('=')[1])

            let item = document.cookie.split(',')[0].split('=')[1].split(" ")
            console.log(counter)
            console.log(item)

            let i;
            let totalAmount = 0
            for(i=0; i<counter; i++)
            {
                let itemCounter = 1
                for(let j = i+1; j<counter; j++)
                {   
                    if(Number(item[j]) == Number(item[i]))
                    {
                        itemCounter +=1;
                    }
                }
                totalAmount += Number(contentTitle[item[i]-1].price) * itemCounter
                orderSaved(contentTitle[item[i]-1],itemCounter)
                i += (itemCounter-1)
            }
         
        }
    }
        else
        {
            console.log('call failed!');
        }
}

httpRequest.open('GET', 'http://localhost:1222/posts', true)
httpRequest.send()
