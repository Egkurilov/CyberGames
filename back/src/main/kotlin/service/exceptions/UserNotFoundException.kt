package com.cybergames.service.exceptions


class UserNotFoundException(userId : Long) : RuntimeException() {
}