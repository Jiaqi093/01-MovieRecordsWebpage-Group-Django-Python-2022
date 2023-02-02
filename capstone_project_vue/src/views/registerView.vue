<template>
    
    <div class="login-page">

            <div class = "left-pic">
                <img class="theme-img" src="../assets/images/loginIMG.png" />
            </div>

            <div class = "right-form">

                <div class = 'logo'>
                    <img class = "logo-img" src = "../assets/images/logo.png">
                </div>


                <div class="form-area">

                    <div class = "welcome-msg">
                            Register new account
                    </div>
                    
                    <form @submit.prevent="submit" div class = "login-form">
                        <label for="email" class = "loginInputLabel">Enter your email</label>
                        <input v-model="data.email" type="email" name="email" placeholder="Enter your email" required/>

                        <label for="username" class = "loginInputLabel">Enter your username</label>
                        <input v-model="data.name" type="text" name="username" placeholder="Enter your username" required/>
                    
                        <label for="password" class = "loginInputLabel">Enter your password</label>
                        <input v-model="data.password" type="password" name="password" placeholder="Enter your password" required/>
                        
                        <div class = "errorMessage"><a>{{message}}</a></div>
                        
                        <br>
                        <br>

                        <div class = "loginSubmitButton"><button type="submit">Register<span></span><span></span><span></span><span></span></button></div>


                    </form>
                    
                    
                </div>

            </div>

    </div>    
    

</template>

<script>

import {useRouter} from "vue-router";
import {reactive, ref} from 'vue';


    export default{
       name: 'register',

       setup() {

            const message = ref('');

            const data = reactive({
                name:'',
                email: '',
                password: ''
            });

            const userData = {
                user_id : ''
            }


            const router = useRouter();

            const submit = async () => {

                await fetch('http://localhost:8000/register', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    credentials: 'include',
                    body: JSON.stringify(data)
                })
                .then((response) => response.json())
                .then((details) => {

                    console.log(details)
                    
                    const detailMessage = details.email[0]

                    if(detailMessage=="user with this email already exists."){
                        message.value = `${detailMessage}`

                    } else {

                        message.value = `${''}`
                        userData.user_id = details.id
                    }
                    
                })

                //no error message can register new account for backend function need and redirect to login
                if(message.value === ''){

                    await fetch('http://localhost:8000/Account/', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            credentials: 'include',
                            body: JSON.stringify(userData)
                    })
                
                   await router.push('/login');
                }
                
            }

            return {
                data,
                message,
                submit
            }
        }

    }


</script>

<style>
    @import '../assets/styles/login.css';
</style>