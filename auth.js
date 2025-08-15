import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut } from 'firebase/auth';

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDOo5pcpVEBGeK1Mk7PjOsJW_fDBhPkl-U",
    authDomain: "bankappointment-a479c.firebaseapp.com",
    projectId: "bankappointment-a479c",
    storageBucket: "bankappointment-a479c.appspot.com",
    messagingSenderId: "318938286613",
    appId: "1:318938286613:web:d815fdd13472a2bb401c1c",
    measurementId: "G-G01PCZ4Q8C"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Google Authentication Provider
const provider = new GoogleAuthProvider();

// Function to sign in with Google
const signInWithGoogle = () => {
    signInWithPopup(auth, provider)
        .then((result) => {
            const user = result.user;
            console.log('Logged in as:', user.displayName);
            window.location.href = "index.html"; // Redirect to index page on successful login
        })
        .catch((error) => {
            console.error("Error during sign-in:", error);
            alert("Error during login. Please try again.");
        });
};

// Function to sign out
const signOutUser = () => {
    signOut(auth)
        .then(() => {
            console.log("User signed out");
            window.location.href = "login.html"; // Redirect to login page
        })
        .catch((error) => {
            console.error("Error during sign-out:", error);
            alert("Error during logout. Please try again.");
        });
};

// Export functions for use in other files
export { auth, provider, signInWithPopup, signOutUser };