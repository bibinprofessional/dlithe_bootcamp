import React from 'react'

function CheckEven(props) {
    if (Number(props.number) % 2 == 0) {
        return (
            <div>
                {props.number}
            </div>
        )
    }

}

export default CheckEven