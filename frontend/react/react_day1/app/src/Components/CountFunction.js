import React, { useState } from 'react'

function CountFunction() {
    const [count, setCount] = useState(0);
    const handleClick = () => {
        setCount(count + 1)
    };

    return (
        <div>
            <p>value :{count}</p>
            <button onClick={handleClick}>Count</button>
        </div>
    )
}

export default CountFunction