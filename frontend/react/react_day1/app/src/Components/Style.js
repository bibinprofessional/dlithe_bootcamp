import React from 'react'
import './Style.css'

export default function Style(props) {
    const primary = props.primary ? 'main' : ''
    const style = {
        border: "3px solid black"
    }
    return (
        <div>
            <h1>hjadsk</h1>
            <h2 className={`${primary} secondary`}>dfds</h2>
            <h3 style={style} >fdsdas</h3>
        </div>
    )
}
