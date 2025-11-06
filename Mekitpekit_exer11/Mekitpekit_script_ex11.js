let mealCost = 0

function calcDelivery(){
	var number_of_people = document.getElementById('numPeople').value
	var number_of_people = parseInt(number_of_people)
	var multipleof50 = Math.ceil(number_of_people / 50);
	if (multipleof50 <= 1) {return [1000, number_of_people]}
		else{
			return [(multipleof50 - 1) * 500 + 1000, number_of_people]
		}
}

function addtoOrder(num){
	mealCost += num
}

function checkOrder(id, price){
	var checkbox = document.getElementById(id);
	if (checkbox.checked) {
		addtoOrder(price);
		return true;
	} else {
		return false;
	}
}

function checkAppetizer(){
	let appetizermessage = "Appetizers:\n"
	var appetizers = ['salad', 'bread', 'tomato', 'mushroom']
	var appetizersprice = [100, 70, 120, 150]
	var appetizersname = ['Salad', 'Bread w/Dip', 'Tomato Surprise', 'Mushroom Bites']

	for (let i = 0; i < appetizers.length; i++){
		var ordered = checkOrder(appetizers[i], appetizersprice[i]);
		if (ordered){
			appetizermessage += "\t" + appetizersname[i] + "\n"
		}
	}
	return appetizermessage
}

function checkmainDishes(){
	let maindishesmessage = "Main Dishes:\n"
	var maindishes = ['roast', 'beef', 'pork', 'marbella', 'chicken', 'roastchick', 'broiled', 'grilledsalmon']
	var maindishesprice = [300, 270, 240, 250, 190, 190, 170, 180]
	var maindishesname = ['Roast Beef', 'Beef Steak', 'Pork Spareribs', 'Pork Marbella', 'Grilled Chicken', 'Roast Chicken', 'Broiled Salmon', 'Grilled Salmon']
	for (let i = 0; i < maindishes.length; i++){
		var ordered = checkOrder(maindishes[i], maindishesprice[i]);
		if (ordered){
			maindishesmessage += "\t" + maindishesname[i] + "\n"
		}
	} 
	return maindishesmessage
}

function checkDesserts(){
	let dessertsmessage = "Desserts:\n"
	var desserts = ['choccake', 'velvetcake', 'lemonbars', 'peanutbars', 'bukopie']
	var dessertsprice = [120, 90, 50, 60, 80]
	var dessertsname = ['Molten Chocolate Cake', 'Red Velvet Cake', 'Lemon Bars', 'Peanut Butter Bars', 'Buko Pie', 'Lemon Meringue Pie']
	for (let i = 0; i < desserts.length; i++){
		var ordered =checkOrder(desserts[i], dessertsprice[i])
		if (ordered){
			dessertsmessage += "\t" + dessertsname[i] + "\n"
		}
	}
	return dessertsmessage
}

function checkRice(){
	let ricesmessage = "Rice:\n"
	var rices = ['plain', 'garlic', 'bagoong']
	var ricesprice = [30, 40, 35]
	var ricesname = ['Plain', 'Garlic', 'Bagoong']
	for (let i = 0; i < rices.length; i++){
		var ordered = checkOrder(rices[i], ricesprice[i])
		if (ordered){
			ricesmessage += "\t" + ricesname[i] + "\n"
		}
	}
	return ricesmessage
}

function checkDrinks(){
	let drinksmessage = "Drinks:\n"
	var drinks = ['cucumber', 'icedtea', 'mangojuice']
	var drinksprice = [60, 50, 70]
	var drinksname = ['Cucumber Lemonade', 'Red Iced Tea', 'Ripe Mango Juice']
	for (let i = 0; i < drinks.length; i++){
		var ordered = checkOrder(drinks[i], drinksprice[i]);
		if (ordered){
			drinksmessage += "\t" + drinksname[i] + "\n"
		}
	}
	return drinksmessage
}

function checkMode(){
	let pickup = document.getElementById("store");
	let delivery = document.getElementById("deliver");
	if (pickup.checked){
		document.getElementById("venue").disabled = true;
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
	
	let delivery_details = "Delivery Details:\n \t" + venue + "\n";

	var num_date = Date.parse(date);
	if (num_date < Date.now()){
		datenotif.innerHTML = "Input a valid date. Date must be in the future.";
	} else {
		datenotif.innerHTML = "";
		delivery_details += 
		"\t" + date + "\n"
	}

	var parts = time.split(":");
	var hours = parseInt(parts[0]);
	if (hours < 6 || hours > 18){
		timenotif.innerHTML = "Delivery is only available between 6am and 6pm.";
	} else {
		timenotif.innerHTML = "";
		if (hours > 12){
		delivery_details += 
		"\t" + time + "AM\n"
		} else {
		delivery_details += 
		"\t" + time + "PM\n"
		}
	}

	return delivery_details
}


function clicksubmit(){
	var mode_of_delivery = checkMode();
	if (mode_of_delivery == "delivery"){
		var delivery_details = getDeliveryDetails();
		var delivery_fee = calcDelivery()
	} else if (mode_of_delivery == "pickup"){
		var delivery_details = "Delivery Details:\n \tStore Pickup\n";
		var delivery_fee = calcDelivery()
		delivery_fee[0] = 0;
	}
	
	var total_appetizer = checkAppetizer()
	var total_maindishes = checkmainDishes()
	var total_desserts = checkDesserts()
	var total_rice = checkRice()
	var total_drinks = checkDrinks()
	alert("Number of people: \t" + delivery_fee[1] + "\n" +
		total_appetizer + total_maindishes + total_desserts + total_rice + total_drinks + delivery_details + "\nMeal Cost: \t" + mealCost + "\nDelivery Fee: \t" + delivery_fee[0] + "\nTotal Cost: \t" + (mealCost + delivery_fee[0])
	)
	mealCost = 0;
}

window.onload = function(){
	checkMode();
}
