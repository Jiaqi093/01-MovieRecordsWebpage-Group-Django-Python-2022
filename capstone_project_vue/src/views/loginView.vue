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
                                Login into your account
                        </div>
                        
                        <form @submit.prevent="submit" class = "login-form">
                            <label for="username" class = "loginInputLabel">Email</label>
                            <input v-model="data.email" type="text" name="email" placeholder="Enter your email" required/>
                        
                            <label for="password" class = "loginInputLabel">Password</label>
                            <input v-model="data.password" type="password" name="password" placeholder="Enter your password" required/>
                            <div class = "errorMessage"><a>{{message}}</a></div>

                            <br>
                            <br>

                            <div class = "loginSubmitButton"><button type="submit">Login now<span></span><span></span><span></span><span></span></button></div>
                            <div class = "loginSubmitButton"><button type="submit">Or signin with google<span></span><span></span><span></span><span></span></button></div>
                            <a href="/#/register">register now</a>

                        </form>
                        
                        
                    </div>

                </div>

    </div>        
    

</template>

<script>

  import {reactive,ref} from 'vue';
  import {useRouter} from "vue-router";


    export default {
      name: "login",
      setup() {


        const message = ref('');

        const data = reactive({
          email: '',
          password: ''
        });


        const router = useRouter();
        

        const submit = async () => {
          await fetch('http://localhost:8000/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            credentials: 'include',
            body: JSON.stringify(data)
          })
          .then((response) => response.json())
          .then((details) => {
            
            const detailMessage = details.detail

            //make sure only related message is printed
            
            message.value = `${detailMessage}`

          })
          
          //if no error with any of the password or username
          if(message.value === 'undefined'){
            await router.push('/');
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