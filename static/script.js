localStorage.clear();
//Check if the "visited" key exists in localStorage



if (!localStorage.getItem("visited")) {
  // First-time visit or first-time visit since download
  // Set the "visited" key in localStorage
  //localStorage.setItem("visited", "true");

  // Redirect to the fitness page for sign up or login
setTimeout(() => {
    window.location.href = "/login/";
  }, 1000);
} else {
   //User has already visited the app
   //Redirect to the main page
  setTimeout(() => {
    window.location.href = "/mainpg/";
  }, 1000);
}