import React, { useState } from 'react'
import InputBox from "../Components/inputBox"

export default function Login() {

    const [username, setUsername] = useState(" ")
    const [password, setPassword] = useState(" ")


    const submit = () => {
       fetch(
        '/login/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                },
            body: JSON.stringify({ username, password })
            }

       ).then(res=>console.log(res))
    }

  return (
    <div className='flex flex-col center  h-full m-10 justify-items-center items-center'>
        
       
            <div className="max-w-180 w-full p-10 bg-white rounded-lg shadow-md">
                <h1 className="text-5xl text-center text-gray-800 font-bold mb-15">Login</h1>
                <InputBox 
                    className=""
                    type="text"
                    label="Username"
                    variable={username}
                    setVar={setUsername}

                />
                
                <InputBox 
                    className=""
                    type="password"
                    label="Password"
                    variable={password}
                    setVar={setPassword}

                />
                
                <button className="w-full mt-2 bg-blue-500 hover:bg-blue-700 text-white font-bold px-10 py-2 text-2xl rounded-xl" onClick={submit}>Submit</button>


            </div>
    
        
    </div>
  )
}
