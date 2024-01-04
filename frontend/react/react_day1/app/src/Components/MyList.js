import React from 'react'

function MyList() {
    const items = ['Bibin', 'Nikhil', 'Shri', 'Varsha', 'Ziya', 'Srujan'];
    return (
        <div style={{ backgroundColor: 'gray' }}>
            <ul>
                {items.map((item, index) => (
                    <li key={index}>Welcome {item}, Index is {index}</li>
                ))}
            </ul>
        </div>
    )
}

export default MyList