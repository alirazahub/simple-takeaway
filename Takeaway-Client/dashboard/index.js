document.querySelector(".jsFilter").addEventListener("click", function () {
  document.querySelector(".filter-menu").classList.toggle("active");
});
//   grid view
document.querySelector(".grid").addEventListener("click", function () {
  document.querySelector(".list").classList.remove("active");
  document.querySelector(".grid").classList.add("active");
  document.querySelector(".products-area-wrapper").classList.add("gridView");
  document
    .querySelector(".products-area-wrapper")
    .classList.remove("tableView");
});
// list view
document.querySelector(".list").addEventListener("click", function () {
  document.querySelector(".list").classList.add("active");
  document.querySelector(".grid").classList.remove("active");
  document.querySelector(".products-area-wrapper").classList.remove("gridView");
  document.querySelector(".products-area-wrapper").classList.add("tableView");
});
// dark mode switch
var modeSwitch = document.querySelector('.mode-switch');
modeSwitch.addEventListener('click', function () {
  document.documentElement.classList.toggle('light');
  modeSwitch.classList.toggle('active');
});

/* Sidebar start here */
let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

closeBtn.addEventListener("click", () => {
  sidebar.classList.toggle("open");
  menuBtnChange();//calling the function(optional)
});

searchBtn.addEventListener("click", () => { // Sidebar open when you click on the search icon
  sidebar.classList.toggle("open");
  menuBtnChange(); //calling the function(optional)
});

// following are the code to change sidebar button(optional)
function menuBtnChange() {
  if (sidebar.classList.contains("open")) {
    closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the icons class
  } else {
    closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");//replacing the icons class
  }
}

/* Sidebar end here */

/* Tab Start Here */
function openTab(event, tabNumber) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the link that opened the tab
  document.getElementById(tabNumber).style.display = "block";
  event.currentTarget.className += " active";
}
/* Tab End Here */

/* Tab two Start here*/
const wrapper = document.querySelector(".wrapper");
const jobCards = document.querySelectorAll(".job-card");
const logo = document.querySelector(".logo");
const jobLogos = document.querySelector(".job-logos");
const jobDetailTitle = document.querySelector(
  ".job-explain-content .job-card-title"
);
const jobBg = document.querySelector(".job-bg");

jobCards.forEach((jobCard) => {
  jobCard.addEventListener("click", () => {
    const number = Math.floor(Math.random() * 10);
    const url = `https://unsplash.it/640/425?image=${number}`;
    jobBg.src = url;

    const logo = jobCard.querySelector("svg");
    const bg = logo.style.backgroundColor;
    console.log(bg);
    jobBg.style.background = bg;
    const title = jobCard.querySelector(".job-card-title");
    jobDetailTitle.textContent = title.textContent;
    jobLogos.innerHTML = logo.outerHTML;
    wrapper.classList.add("detail-page");
    wrapper.scrollTop = 0;
  });
});

logo.addEventListener("click", () => {
  wrapper.classList.remove("detail-page");
  wrapper.scrollTop = 0;
  jobBg.style.background = bg;
});
/* Tab two End here*/

function addProduct() {
  const productName = document.getElementById("productName").value;
  const productDescription = document.getElementById("productDescription").value;
  const productPrice = document.getElementById("productPrice").value;
  const productImage = document.getElementById("productImage").value;
  const brand = document.getElementById("brand").value;

  // You can perform any further actions with the form data here, like sending it to a server using AJAX.

  // For this example, we'll just log the data to the console.
  console.log("Product Name:", productName);
  console.log("Product Description:", productDescription);
  console.log("Product Price:", productPrice);
  console.log("Product Image URL:", productImage);

  const post = {
    name: productName,
    preview: productImage,
    photos: productImage,
    description: productDescription,
    size: 1,
    isAccessory: false,
    brand: brand,
    price: parseFloat(productPrice) // Assuming productPrice is a numeric value
  };

  fetch('http://localhost:1222/add', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(post)
  })
    .then(response => response.json())
    .then(data => {
      console.log('API Response:', data);
      // You can perform further actions with the response from the API here, if needed.
    })
    .catch(error => {
      console.error('Error:', error);
    });

  // Clear the form fields after submitting
  document.getElementById("productName").value = "";
  document.getElementById("productDescription").value = "";
  document.getElementById("productPrice").value = "";
  document.getElementById("productImage").value = "";
}
function dynamicProducts() {
  let boxDiv = document.createElement("div");
  boxDiv.class = "products-row";

  let boxLink = document.createElement("button");
  boxLink.href = "/contentDetails.html?" + ob.id;

  let imgTag = document.createElement("img");
  // imgTag.id = 'image1'
  // imgTag.id = ob.photos
  imgTag.src = ob.preview;

  let detailsDiv = document.createElement("div");
  detailsDiv.id = "details";

  let h3 = document.createElement("h3");
  let h3Text = document.createTextNode(ob.name);
  h3.appendChild(h3Text);

  let h4 = document.createElement("h4");
  let h4Text = document.createTextNode(ob.brand);
  h4.appendChild(h4Text);

  let h2 = document.createElement("h2");
  let h2Text = document.createTextNode("$  " + ob.price);
  h2.appendChild(h2Text);

  boxDiv.appendChild(boxLink);
  boxLink.appendChild(imgTag);
  boxLink.appendChild(detailsDiv);
  detailsDiv.appendChild(h3);
  detailsDiv.appendChild(h4);
  detailsDiv.appendChild(h2);

  return boxDiv;
}
