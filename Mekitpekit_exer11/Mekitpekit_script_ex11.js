let mealCost = 0

function calcDelivery(){
	var number_of_people = document.getElementById('numPeople').value; 
	var number_of_people = parseInt(number_of_people)
	var multipleof50 = Math.ceil(number_of_people / 50); //round up
	if (multipleof50 <= 1) {return [1000, number_of_people]} 
		else{
			return [(multipleof50 - 1) * 500 + 1000, number_of_people];
		}
}

function addtoOrder(num){
	mealCost += num;
}

function checkOrder(id, price){
	var checkbox = document.getElementById(id);
	if (checkbox.checked) { //if element is checked
		addtoOrder(price);
		return true; //for checking later
	} else {
		return false;
	}
}

function checkAppetizer(){
	//loop through apppetizers using its id and get the name and price
	let appetizermessage = "Appetizers:\n";
	var appetizers = ['salad', 'bread', 'tomato', 'mushroom'];
	var appetizersprice = [100, 70, 120, 150];
	var appetizersname = ['Salad', 'Bread w/Dip', 'Tomato Surprise', 'Mushroom Bites'];

	for (let i = 0; i < appetizers.length; i++){
		var ordered = checkOrder(appetizers[i], appetizersprice[i]); //get the corresponding element and call checkOrder
		if (ordered){
			appetizermessage += "\t" + appetizersname[i] + "\n"; // add to message
		}
	}
	return appetizermessage; //output message
}

function checkmainDishes(){
	//loop through main dishes using its id and get the name and price
	let maindishesmessage = "Main Dishes:\n";
	var maindishes = ['roast', 'beef', 'pork', 'marbella', 'chicken', 'roastchick', 'broiled', 'grilledsalmon'];
	var maindishesprice = [300, 270, 240, 250, 190, 190, 170, 180];
	var maindishesname = ['Roast Beef', 'Beef Steak', 'Pork Spareribs', 'Pork Marbella', 'Grilled Chicken', 'Roast Chicken', 'Broiled Salmon', 'Grilled Salmon'];
	for (let i = 0; i < maindishes.length; i++){
		var ordered = checkOrder(maindishes[i], maindishesprice[i]);
		if (ordered){
			maindishesmessage += "\t" + maindishesname[i] + "\n";
		}
	} 
	return maindishesmessage;
}
//use the same logic 
function checkDesserts(){
	let dessertsmessage = "Desserts:\n";
	var desserts = ['choccake', 'velvetcake', 'lemonbars', 'peanutbars', 'bukopie', 'meringue'];
	var dessertsprice = [120, 90, 50, 60, 50, 70];
	var dessertsname = ['Molten Chocolate Cake', 'Red Velvet Cake', 'Lemon Bars', 'Peanut Butter Bars', 'Buko Pie', 'Lemon Meringue Pie'];
	for (let i = 0; i < desserts.length; i++){
		var ordered =checkOrder(desserts[i], dessertsprice[i]);
		if (ordered){
			dessertsmessage += "\t" + dessertsname[i] + "\n";
		}
	}
	return dessertsmessage;
}

function checkRice(){
	let ricesmessage = "Rice:\n";
	var rices = ['plain', 'garlic', 'bagoong'];
	var ricesprice = [30, 40, 35];
	var ricesname = ['Plain', 'Garlic', 'Bagoong'];
	for (let i = 0; i < rices.length; i++){
		var ordered = checkOrder(rices[i], ricesprice[i]);
		if (ordered){
			ricesmessage += "\t" + ricesname[i] + "\n";
		}
	}
	return ricesmessage;
}

function checkDrinks(){
	let drinksmessage = "Drinks:\n";
	var drinks = ['cucumber', 'icedtea', 'mangojuice'];
	var drinksprice = [60, 50, 70];
	var drinksname = ['Cucumber Lemonade', 'Red Iced Tea', 'Ripe Mango Juice'];
	for (let i = 0; i < drinks.length; i++){
		var ordered = checkOrder(drinks[i], drinksprice[i]);
		if (ordered){
			drinksmessage += "\t" + drinksname[i] + "\n";
		}
	}
	return drinksmessage;
}

function checkMode(){
	let pickup = document.getElementById("store");
	let delivery = document.getElementById("deliver");
	if (pickup.checked){ // if store pickup is chosen
		document.getElementById("venue").disabled = true; //disable the elements
		document.getElementById("partydate").disabled = true;
		document.getElementById("partytime").disabled = true;
		return "pickup";
	} else if (delivery.checked){
		document.getElementById("venue").disabled = false;
		document.getElementById("partydate").disabled = false;
		document.getElementById("partytime").disabled = false;
		return "delivery";
	}}

function getDeliveryDetails(){
	var venue = document.getElementById("venue").value; 
	var date = document.getElementById("partydate").value; 
	var time = document.getElementById("partytime").value;
	var datenotif = document.getElementById("datenotif");
	var timenotif = document.getElementById("timenotif");
	
	let delivery_details = "Delivery Details:\n\t Delivery\n \t" + venue + "\n";

	var num_date = Date.parse(date); //convert date to a number
	if (num_date < Date.now()){ // gets current date and checks if in the past
		datenotif.innerHTML = "Input a valid date. Date must be in the future.";
	} else {
		datenotif.innerHTML = ""; //clear the warning
		delivery_details +=  
		"\t" + date + "\n";
	}

	var parts = time.split(":"); //splits the time into hour and minute
	var hours = parseInt(parts[0]);
	if (hours < 6 || hours > 18){ // if hour is less than 6am or greater than 6pm
		timenotif.innerHTML = "Delivery is only available between 6am and 6pm.";
	} else {
		timenotif.innerHTML = "";
		if (hours < 12){
		delivery_details += 
		"\t" + time + "AM\n";
		} else {
		delivery_details += 
		"\t" + time + "PM\n";
		}
	}

	return delivery_details;
}


function clicksubmit(){
	var mode_of_delivery = checkMode(); //call and store the value of mode of delivery
	if (mode_of_delivery == "delivery"){
		var delivery_details = getDeliveryDetails();
		var delivery_fee = calcDelivery();
	} else if (mode_of_delivery == "pickup"){
		var delivery_details = "Delivery Details:\n \tStore Pickup\n";
		var delivery_fee = calcDelivery();
		delivery_fee[0] = 0; //0 delivery fee if store pickup
	}
	//store messages from checking the orders
	var total_appetizer = checkAppetizer(); 
	var total_maindishes = checkmainDishes();
	var total_desserts = checkDesserts();
	var total_rice = checkRice();
	var total_drinks = checkDrinks();
	alert("Number of people: \t" + delivery_fee[1] + "\n" +
		total_appetizer + total_maindishes + total_desserts + total_rice + total_drinks + delivery_details + 
		"\nMeal Cost: \t" + mealCost + 
		"\nDelivery Fee: \t" + delivery_fee[0] + 
		"\nTotal Cost: \t" + (mealCost + delivery_fee[0])
	);
	mealCost = 0; //reset meal cost after submit
}

window.onload = function(){
	checkMode();
}
