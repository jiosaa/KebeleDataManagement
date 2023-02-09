document.getElementById("id_phone_number").type = "number";
const firstname = document.getElementById("id_first_name");
firstname.addEventListener('keypress',(event)=>{
      let inputedValue = event.charCode;
      if(!(inputedValue>=65&&inputedValue<=122) && (inputedValue =32 && inputedValue !=0)){
          event.preventDefault() 
      }
});
    
const middlename = document.getElementById("id_middle_name");
middlename.addEventListener('keypress',(event)=>{
    let inputedValue = event.charCode;
    if(!(inputedValue>=65&&inputedValue<=122) && (inputedValue =32 && inputedValue !=0)){
        event.preventDefault() 
    }
   
});
     const lastname = document.getElementById("id_last_name");
   lastname.addEventListener('keypress',(event)=>{
    let inputedValue = event.charCode;
    if(!(inputedValue>=65&&inputedValue<=122) && (inputedValue =32 && inputedValue !=0)){
        event.preventDefault() 
    }
          }



          );
 
          const mothername = document.getElementById("id_mother_name");
          mothername.addEventListener('keypress',(event)=>{
            let inputedValue = event.charCode;
            if(!(inputedValue>=65&&inputedValue<=122) && (inputedValue!=32 && inputedValue !=0)){
                event.preventDefault() 
            }

                 });           
let errorFound=(valid_age ,phone_number)=>{

    console.log(valid_age,phone_number);
    document.getElementById('form').addEventListener("submit",function(event){
        if(valid_age && phone_number){
            document.myform.submit()   
        }
    
        else{
            event.preventDefault() 
     
            }
       });
    }


function validator(){
    let valid_phone_number = false
    let valid_age = false
    document.getElementById('id_phone_number').addEventListener('input',()=>{
        let  displayPhoneNumberError = document.getElementById("phone_number_error");
               let phone_number = document.getElementById('id_phone_number').value
               let  phone_number_length =  phone_number.toString().length
              
               if(phone_number_length  < 9){
                
                   displayPhoneNumberError.style.display = "block";
                   displayPhoneNumberError.innerHTML = `Invalid Phone Number: its only ${phone_number_length} check and correct` ;
                   valid_phone_number = false
                }
           
           
               else if( phone_number_length   == 10 && phone_number.toString().charAt(0) != 0 ){
                   displayPhoneNumberError.style.display = "block";
                    displayPhoneNumberError.innerHTML = `Invalid Phone Number : Please Use This Format : 0912345678 or 912345678`;
                    valid_phone_number = false       
                  }
           
           
               else if( phone_number_length  == 10 && phone_number.toString().charAt(0) == 0 ){
                   valid_phone_number = true
                   phone_number = parseInt(phone_number);
                   displayPhoneNumberError.style.display = "none";
                }
                   
           
               else if( phone_number_length  > 10){
                   displayPhoneNumberError.style.display = "block";
                    displayPhoneNumberError.innerHTML = "Invalid Phone Number: Please Insert In This Format : 0912345678 or 912345678 ";
                    valid_phone_number = false
                 }
           
           
             else {
                   displayPhoneNumberError.style.display = "none";
       
             }
             errorFound(valid_age,valid_phone_number)  
          
            });
       
                const age = document.getElementById("id_age");
                age.addEventListener('input',(e)=>{
                         if (age.value <= 18 || age.value >= 150 ) {
                            valid_age = false;
                         }
                         else{
                            valid_age = true;
                         }
                         
     
errorFound(valid_age,valid_phone_number);       
                       

});      

}

validator();