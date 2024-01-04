import React, { useState } from 'react'

function ReverseCounter() {
    const [count, setCount] = useState(10);
    const handleClick = () => {
        setCount(count - 1)
    };

    return (
        <div>
            <p>value :{count}</p>
            <button onClick={handleClick}>Count</button>
        </div>
    )
}

export default ReverseCounter