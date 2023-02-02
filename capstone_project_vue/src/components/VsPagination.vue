<template>
    <div>
        <div class = "pagination-row">

            <button class="pagination-button" @click="onClickPage(pageNumber=pageNumber-1)">Previous</button>
            <span v-for = "(item,index) in Array(totalPages)" :key="index">
                <button :class="['pagination-button', pageNumber === index + 1 ? 'active':'']" @click="onClickPage(pageNumber=index+1)">
                    {{index + 1}}
                </button>
            </span>
            <button class="pagination-button" @click="onClickPage(pageNumber=pageNumber+1)">Next</button>

        </div>
        
    </div>
</template>
  
<script>
  export default {
    name: 'VsPagination',

    data(){
        return{
            pageNumber: 1
        }
    },

    props: {
        maxVisibleButtons: {
            type: Number,
            required: false,
            default: 3
        },  
          
        totalPages: {
            type: Number,
            required: true
        },
        perPage: {
            type: Number,
            required: true
        },
        currentPage: {
            type: Number,
            required: true
        }
    },

    computed: {
        
    },
    methods:{
        onClickPage(page) {
            this.$emit('pagechanged', page);
        }
    }
  }
</script>
  

<style scoped>
    
    .pagination-button{
        padding:8px;
        margin:2px;
        border-radius: 3px;
        cursor: pointer;

        background-color: white;
        border-color: black;
        box-shadow: 2px 2px black;
        margin-left: 5px;
    }

    .pagination-button:hover{
        box-shadow: 5px 5px black;
        left:-3px;
        top:-3px;

        background-color: #171B72;
        color:white;
        cursor:pointer;

    }
    .active{
        box-shadow: 5px 5px black;
        left:-3px;
        top:-3px;

        background-color: #171B72;
        color:white;

        cursor:default;
    }
</style>
  