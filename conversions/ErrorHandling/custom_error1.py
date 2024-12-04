def chek_number(number):

    if number>0:
         
         return "+ve"

    elif number<0:

        return "-ve"
    elif number==0:
        return "zreo"

def test_num_chck():

      assert chek_number(10)=="+ve","+ve number check failed"

      assert chek_number(-10)=="-ve","+ve number check failed"

      assert chek_number(10)=="zero","zero number check failed"

      
test_num_chck()

      


      
