<template>

  <div class="wrapper">

    <div class="passwordChange-page">

    <form
      class="formPWD"
      @submit.prevent="submit"
    >

      <p style="font-size: 30px">Change Password</p>

      <label> New Password </label>
      <input
        type="password"
        name="newPwd"
        placeholder="Enter new password"
        required
      />

      <label> Confirm Password </label>
      <input
        type="password"
        name="confirm"
        placeholder="Confirm new password"
        required
        v-model = "data.newPassword"
      />

      <div class="changePWDPrompt">
        
      </div>

      <div class="pwdSubmitButton"><button
          type="submit"
        
        >Change</button></div>

      <div class="backbutton"><a href="/#/"> Back </a></div>

    </form>

    </div>
    
  </div>

</template>


<script>
import { useRouter } from 'vue-router';
import { reactive } from 'vue';

    export default {
        name: "changePassword",

        methods:{
          async submit () {


          await fetch('http://localhost:8000/user', {
              method: 'POST',
              mode: 'cors',
              headers: { 'Content-Type': 'application/json' },
              credentials: 'include',
              body: JSON.stringify(this.data)
          })
          .then((response) => response.json())
          .then( function(result){

              console.log(result)
          })

          this.router.push('/')

          },
        }, 

        setup() {
        const router = useRouter()


        const data = reactive({
          newPassword: '',

        })


        return {
            data,
            router,
        }
    }

    }

</script>

<style>
    @import '../assets/styles/updatePWD.css';

</style>