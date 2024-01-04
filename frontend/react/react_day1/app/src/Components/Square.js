import React, { useState } from 'react'

function Square() {
    const [count, setCount] = useState(2);
    const handleClick = () => {
        setCount(count * count)
    };

    return (
        <div>
            <p>value :{count}</p>
            <button onClick={handleClick}>Count</button>
        </div>
    )
}

export default Square