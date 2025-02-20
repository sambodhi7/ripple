import React from 'react'

export default function InputBox({className,label,type,variable,setVar}) {
  return (
    <>
       <label className={`block text-gray-700 text-4xl font-bold mb-2 ${className}` }htmlFor={label}>{label}</label>
        <input className="block w-full p-2 mb-4 text-gray-700 placeholder-gray -400 border border-gray-300 rounded-lg" 
        type={type} 
        id={label} 
        name={label } 
        value={variable} 
        onChange={(e) => setVar (e.target.value)} 
        placeholder={label}
        />

    </>
  )
}
