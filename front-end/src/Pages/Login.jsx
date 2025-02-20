import React, { useState } from 'react'

export default function Login() {

    const [username, setUsername] = useState(" ")
    const [password, setPassword] = useState(" ")


    const submit = () => {
        console.log(
            `Username: ${username}, Password: ${password}`
        )
    }

  return (
    <div className='flex flex-col center  h-full m-10'>
        <h1 className="text-5xl text-center text-gray-800 font-bold mb-4">Login</h1>
       
            <div className="m-4 ">
               <input type= "text" className="border-2 rounded" value={username} onChange={e=>{ setUsername(e.target.value);
                console.log(e.target.value)}
            }/>
                <button className='bg-grey' onClick={submit}>Submit</button>


            </div>
    
        
    </div>
  )
}
