namespace Demo;

/// <summary>
/// Vài phép biến đổi chuỗi đơn giản.
/// </summary>
/// <remarks>
/// Cố ý để trống chỗ cho việc mở rộng: repo này tồn tại để agent có thứ gì đó thật để sửa.
/// </remarks>
public static class StringUtils
{
    /// <summary>Đảo ngược một chuỗi.</summary>
    public static string Reverse(string value)
    {
        ArgumentNullException.ThrowIfNull(value);

        char[] characters = value.ToCharArray();
        Array.Reverse(characters);

        return new string(characters);
    }

    /// <summary>Kiểm tra một chuỗi có đối xứng hay không, bỏ qua hoa thường và khoảng trắng.</summary>
    public static bool IsPalindrome(string value)
    {
        ArgumentNullException.ThrowIfNull(value);

        string normalized = new string(value.Where(c => !char.IsWhiteSpace(c)).ToArray()).ToLowerInvariant();
        char[] reversed = normalized.ToCharArray();
        Array.Reverse(reversed);

        return normalized == new string(reversed);
    }
}
