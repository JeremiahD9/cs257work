function generateNum()
{
	randNumText = document.getElementById("generateNum");
	let min = document.getElementById("minNum").value * 1;
    let max = document.getElementById("maxNum").value * 1;
	let randNum = Math.floor(Math.random() * (max - min + 1) ) + min;
  
  randNumText.innerHTML = randNum;
}